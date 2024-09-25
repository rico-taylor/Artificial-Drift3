import sqlite3

connection = sqlite3.connect("data2.db")

cursor = connection.cursor()

DEFAULT_TIME = 0

#this defines the table with two columns - gamer_name and time
cursor.execute("""
CREATE TABLE IF NOT EXISTS lap_times(
    gamer_name TEXT,
    time FLOAT
)
""")

def new_player_db(player_name):
    cursor.execute("""
    INSERT INTO lap_times VALUES
    ('{}', {})             
    """.format(player_name, 0))

    connection.commit()

def delete_player_db(player_name):
    cursor.execute("""
    DELETE FROM lap_times
        WHERE gamer_name = '{}'
    """.format(player_name))

    connection.commit()

def new_pb():
    pass

def get_db():
    cursor.execute("SELECT * FROM lap_times")
    results = cursor.fetchall()
    return results


new_player_db("Rico Taylor")
print(get_db())