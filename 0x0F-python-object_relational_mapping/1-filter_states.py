#!/usr/bin/python3
"""
that script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name \
            LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
