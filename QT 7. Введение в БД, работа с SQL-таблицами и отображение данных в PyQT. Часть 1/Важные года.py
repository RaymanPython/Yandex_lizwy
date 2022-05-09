import sqlite3

a = []
b = []
name = input()
con = sqlite3.connect(name)
cur = con.cursor()
s = """SELECT films.year FROM films
    WHERE films.title LIKE 'Х%'"""
cur.execute(s)
result = cur.fetchall()
for i in result:
    a.append(i[0])
for i in a:
    if i not in b:
        print(i)
    else:
        pass
    b.append(i)
con.close()
