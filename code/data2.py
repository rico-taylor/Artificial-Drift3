import sqlite3

connection = sqlite3.connect("data2.db")

cursor = connection.cursor()

DEFAULT_TIME = 0

#this defines the table with two columns - gamer_name and time
cursor.execute("""
CREATE TABLE IF NOT EXISTS lap_times(
    gamer_name TEXT,
    password VARCHAR, 
    date VARCHAR,
    time FLOAT
)
""")

def new_player_db(player_name, password):
    cursor.execute("""
    INSERT INTO lap_times VALUES
    ('{}', '{}', '{}', {})             
    """.format(player_name, password, 0, 0))

    connection.commit()

def delete_player_db(player_name):
    cursor.execute("""
    DELETE FROM lap_times
        WHERE gamer_name = '{}'
    """.format(player_name))

    connection.commit()

def new_pb():
    pass

def check_if_in_db(player_name, password):
    cursor.execute("""
    SELECT * FROM lap_times
    WHERE gamer_name = '{}'
""".format(player_name))
    players = cursor.fetchall() 
    try:
        player = players[0]
        if password == player[1]:
            print("the passwords match")
        else:
            print("the passwords don't match")
    except:
        print("username not found")

def check_username_db(player_name):
    cursor.execute("""
    SELECT * FROM lap_times
    WHERE gamer_name = '{}'
""".format(player_name))
    players = cursor.fetchall() 
    if len(players) > 0:
        return True
    else:
        return False

def get_lap_time_db(player_name):
    cursor.execute("""
    SELECT * FROM lap_times
    WHERE gamer_name = '{}'
""".format(player_name))
    all = cursor.fetchall() 
    player = all[0]
    best_time = player[3]
    return best_time

def get_lap_date_db(player_name, column):
    cursor.execute("""
    SELECT * FROM lap_times
    WHERE gamer_name = '{}'
""".format(player_name))
    all = cursor.fetchall() 
    player = all[0]
    date = player[column]
    return date

def update_lap_and_date_db(player_name, new_lap_time, new_date):
    cursor.execute("""
    UPDATE lap_times
    SET date = '{}', time = {}
    WHERE gamer_name = '{}'
""".format(new_date, new_lap_time, player_name))
    
    connection.commit()


def update_password_db(player_name, new_password):
    cursor.execute("""
    UPDATE lap_times
    SET password = '{}'
    WHERE gamer_name = '{}'
""".format(new_password, player_name))
    
    connection.commit()

def get_db():
    cursor.execute("SELECT * FROM lap_times")
    results = cursor.fetchall()
    return results

#update_password_db("Rico", "passypassy")
#new_player_db("Rico Taylor", "password123")
#delete_player_db("Rico Taylor")
print(get_lap_time_db("Rico"))
#check_username_db("Rico Taylor")
print(get_db())