import sqlite3

name = input()
con = sqlite3.connect(name)
cur = con.cursor()
s = '''SELECT title FROM films WHERE genre IN (SELECT id FROM genres WHERE title IN
            ('музыка', 'анимация')) and year >= 1997'''
cur.execute(s)
result = cur.fetchall()
for elem in result:
    print(elem[0])
con.close()
