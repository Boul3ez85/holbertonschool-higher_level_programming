#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=dbname,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name " +
                "FROM cities " +
                "INNER JOIN states " +
                "ON cities.state_id = states.id " +
                "WHERE states.name = %s ORDER BY cities.id ASC;", (name,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
