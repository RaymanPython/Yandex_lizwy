import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    res = cur.execute("""UPDATE films
        SET duration = 100
        WHERE genre = (SELECT id FROM genres
        WHERE title = 'мюзикл') and duration >= 100""")
    conn.commit()
    conn.close()
