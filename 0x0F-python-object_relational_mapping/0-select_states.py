#!/usr/bin/pyhton3

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=databas)

    cursordb = db.cursor()
    cursordb.execute("SELECT * FROM states")

    rows = cursordb.fetchall()

    for row in rows:
        print(row)

    cursordb.close()
    db.close()
