#!/usr/bin/python3
"""

script that takes in an argument
and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument.
"""


from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    """conncet to db and run the query then print the result"""
    db = connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id;".format(argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
