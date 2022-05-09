import sqlite3

name = input()
c = sqlite3.connect(name)
cur = c.cursor()
s = """SELECT films.title FROM films 
    WHERE films.title LIKE '%?'"""
cur.execute(s)
result = cur.fetchall()
for i in result:
    print(i[0])
c.close()
