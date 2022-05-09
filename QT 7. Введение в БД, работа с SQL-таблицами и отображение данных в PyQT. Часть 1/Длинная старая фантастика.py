import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    res = cur.execute("""DELETE FROM films
        WHERE genre = (SELECT id FROM genres
        WHERE title = 'фантастика')
        and year < 2000 and duration > 90""")
    conn.commit()
    conn.close()
