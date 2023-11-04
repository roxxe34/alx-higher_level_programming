#!/usr/bin/python3

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
curr = db.cursor()
curr.execute(f"""
    SELECT states 
    FROM {sys.argv[3]}
    ORDER by states.id ASC
""")
print(curr.fetchall())
