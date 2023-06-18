#!/usr/bin/python3
"""
that script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s \
            ORDER BY id ASC", (sys.argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
