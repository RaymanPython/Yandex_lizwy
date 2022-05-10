import sqlite3


class HeadHunter:

    def __init__(self, db_name):
        self.db_name = db_name

    def crafts(self, surname):
        query = f'SELECT DISTINCT job FROM occupations, persons, professions WHERE surname="{surname}" ' \
                f'AND occupations.job_id=professions.job_id AND occupations.person_id=persons.id ORDER BY job'
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute(query)
        return list(map(lambda x: x[0], result))

    def persons(self, craft):
        query = f'SELECT DISTINCT name, surname FROM occupations, persons, professions WHERE job="{craft}" ' \
                f'AND occupations.job_id=professions.job_id AND occupations.person_id=persons.id ORDER BY name, surname'
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        result = cur.execute(query)
        return list(map(' '.join, result))
