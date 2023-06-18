#!/usr/bin/python3
"""
that script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name='{}' \
            ORDER BY id ASC".format(sys.argv[4])

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
