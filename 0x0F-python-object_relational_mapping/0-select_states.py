#!/usr/bin/python3

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
curr = db.cursor()
curr.execute("SELECT * FROM `states`")
[print(state) for state in curr.fetchall()]