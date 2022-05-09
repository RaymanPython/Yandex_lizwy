import sqlite3


def get_result(name):
    c = sqlite3.connect(name)
    b = c.cursor()
    a = b.execute("""DELETE FROM films
        WHERE genre = (SELECT id FROM genres
        WHERE title = 'комедия' )""")
    c.commit()
    c.close()
