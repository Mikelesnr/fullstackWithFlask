import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)

cursor = connection.cursor()

cursor.execute(
    """ INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
            'Gordon',
            'Ramsay',
            'red'
        );"""
)


cursor.execute(
    """ INSERT INTO users(
        username,
        password,
        favorite_color
        )VALUES(
            'Jamie',
            'Oliver',
            'green'
    );"""
)

connection.commit()
cursor.close()
connection.close()
