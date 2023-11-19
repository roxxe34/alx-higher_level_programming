#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="127.0.0.1", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    data = curr.fetchall()
    for row in data:
        print(row)
    curr.close()
    db.close()
