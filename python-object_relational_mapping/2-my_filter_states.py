#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for row in results:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
