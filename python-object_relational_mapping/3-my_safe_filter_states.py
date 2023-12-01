#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. Safe from
MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query with parameterized inputs to prevent SQL
    # injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows and display the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)
