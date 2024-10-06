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

def get_row_db(username): #gets the row based on the username
    cursor.execute("""
    SELECT * FROM lap_times
    WHERE gamer_name = '{}'
""".format(username))
    players = cursor.fetchall() 
    player = players[0]
    return player

def sort_alphabetical(data):
    name_list = []
    for row in data:
        username, password, date, time = row
        name_list.append(username)
    ordered_names = sorted(name_list)
    new_data = []
    for x in ordered_names:
        new_data.append(get_row_db(x))
    return new_data

from datetime import datetime

def sort_tuples_by_date(tuples_list):
    # Define a function to convert date from DD-MM-YYYY to a sortable format
    def convert_date(date_str):
        return datetime.strptime(date_str, "%d-%m-%Y")

    sorted_list = sorted(tuples_list, key=lambda x: convert_date(x[0]), reverse=True)
    
    return sorted_list

def sort_by_date(data):
    date_list = []
    reject_list = []
    for row in data:
        username, password, date, time = row
        date_list.append((date, username))
    for x in date_list:
        if x[0] == '0':
            reject_list.append(x)
            date_list.remove(x)
    date_list = sort_tuples_by_date(date_list)
    new_data = []
    for x in date_list:
        new_data.append(get_row_db(x[1]))
    new_data += reject_list
    return new_data
    
#list all data sorted by lap times
def sort_by_lap_times(self, data):
    rejects_list = []
    valid_data_list = []
    for x in data:
        if x[3] == 0.0:
            rejects_list.append(x)
        else:
            valid_data_list.append(x)

    sorted_list = sorted(valid_data_list, key=lambda x: x[3])
    new_data = sorted_list + rejects_list
    
    return new_data


print(get_db())
print()
print(sort_by_lap_times(get_db()))