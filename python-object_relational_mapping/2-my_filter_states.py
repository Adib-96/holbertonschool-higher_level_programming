#!/usr/bin/python3
"""
a script that takes in an argument
and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


from MySQLdb import connect
from sys import argv

if __name__ == "__main__":
    """conncet to db and run the query then print the result"""
    db = connect(
        user=argv[1],
        password=argv[2],
        database=argv[3],
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states  \
            WHERE BINARY `name` = '{}' ;\
                ".format(argv[4]))
    [print(state) for state in cursor.fetchall()]
