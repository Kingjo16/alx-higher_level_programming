#!/usr/bin/python3
"""Script that lists the states of all the database."""

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
    cursordb.execute("""SELECT cities.name FROM
                     cities INNER JOIN states ON states.id=cities.state_id
                     WHERE states.name=%s""", (state_name,))
    ro = cursordb.fetchall()
    ciy = [row[0] for row in ro]
    print(*ciy, sep=", ")
    cursordb.close()
    db.close()
