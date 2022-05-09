import sqlite3


def get_result(name):
    c = sqlite3.connect(name)
    b = c.cursor()
    a = b.execute("""UPDATE films
                     SET duration = '42'
                     WHERE duration = '' """).fetchall()
    c.commit()
    c.close()
