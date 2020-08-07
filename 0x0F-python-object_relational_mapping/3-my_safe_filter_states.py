#!/usr/bin/python3

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8", user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute ("SELECT * FROM states WHERE name = '" + argv[4] + "' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print (row)

    cur.close()
    db.close()

