#!/usr/bin/python3
"""Script that lists all the cities of the database."""

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password,
                         db=database, port=3306)

    cursordb = db.cursor()
    cursordb.execute("""SELECT cities.id, cities.name, states.name FROM
                     cities INNER JOIN states ON states.id=cities.state_id""")

    rows = cursordb.fetchall()

    for row in rows:
        print(row)

    cursordb.close()
    db.close()
