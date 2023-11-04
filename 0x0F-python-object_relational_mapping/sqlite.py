import sqlite3

conn = sqlite3.connect('mydb.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             age integer
#             )""")
c.execute("INSERT INTO employees VALUES('hamza', 'farissi', '22')")
conn.commit()
conn.close()