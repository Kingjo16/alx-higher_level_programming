#!/usr/bin/python3
"""Script that Delates an injection record table."""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)

    cursordb = db.cursor()
    cursordb.execute("SELECT * FROM states WHERE name LIKE %s", (state_name, ))

    rows = cursordb.fetchall()

    for R in rows:
        print(R)
    cursordb.close()
    db.close()
