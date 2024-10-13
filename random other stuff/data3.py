import sqlite3

connection = sqlite3.connect("data3.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS actions (
    action_type TEXT,
    date VARCHAR
)
""")

connection.commit()

def new_data_entry(action, date):
    cursor.execute("""
    INSERT INTO actions VALUES
    ('{}', '{}', '{}', {})             
    """.format(action, date, 0, 0))

    connection.commit()

def get_db():
    cursor.execute("SELECT * FROM lap_times")
    results = cursor.fetchall()
    return results