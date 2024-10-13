import sqlite3

class Person:

    def __init__(self, id_number=1, first="",last="",age=1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect("mydata.db")
        self.cursor = self.connection.cursor()

    def load_person(self):
        self.cursor.execute("""
        SELECT * FROM persons
        """)

        results = self.cursor.fetchone()

        self.id_number = results[1]
        self.first = results[2]
        self.last = results[3]
        self.age = results[4]

p1 = Person()
p1.load_person()
print(p1.first)

connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()

#cursor.execute("""
#SELECT * FROM persons
#WHERE last_name = 'Smith'
#""")

#rows = cursor.fetchall()
#print(rows)

connection.commit()