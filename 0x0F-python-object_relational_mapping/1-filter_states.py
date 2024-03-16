#!/usr/bin/python3
"""Script that lists the states of the database and filter what is needed."""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)

    cursordb = db.cursor()
    cursordb.execute("""SELECT * FROM states WHERE name
                     LIKE 'N%' ORDER BY id ASC""")

    rows = cursordb.fetchall()

    for row in rows:
        print(row)

    cursordb.close()
    db.close()
