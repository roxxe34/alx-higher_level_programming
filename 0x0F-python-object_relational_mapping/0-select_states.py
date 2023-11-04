#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    data = curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in data:
        print(row)