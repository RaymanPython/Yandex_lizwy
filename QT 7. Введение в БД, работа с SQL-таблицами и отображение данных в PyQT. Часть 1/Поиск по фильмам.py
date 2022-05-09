import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
s = '''SELECT title FROM films WHERE genre=(SELECT id FROM genres WHERE 
    title = 'детектив') AND year BETWEEN 1995 AND 2000'''
cur.execute(s)
result = cur.fetchall()
for i in result:
    print(i[0])
con.close()
