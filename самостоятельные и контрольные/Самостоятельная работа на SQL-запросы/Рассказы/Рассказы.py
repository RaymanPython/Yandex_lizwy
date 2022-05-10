import sqlite3

place = input()
query = f'SELECT event, year FROM Data WHERE place=="{place}" ORDER BY event'
place_events = []
db_name = 'events_to_talk.db'
con = sqlite3.connect(db_name)
cur = con.cursor()
result = cur.execute(query).fetchall()
for elem in result:
    place_events.append({'event': elem[0], 'year': elem[1]})
con.close()
