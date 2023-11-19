#!/usr/bin/python3
""" Script that lists all values in the states table of hbtn_0e_0_usa
where name matches the argument """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                 (sys.argv[4],))
    data = curr.fetchall()
    for row in data:
        print(row)
    curr.close()
    db.close()
