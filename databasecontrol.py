import sqlite3
import pandas as pd

conn = sqlite3.connect("user_database")
c = conn.cursor()
conn2 = sqlite3.connect("gmail_database")
c2 = conn2.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS user_information
          ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [password] TEXT, [audioPreference], x [TEXT], y [TEXT])
          ''')

c2.execute('''
          CREATE TABLE IF NOT EXISTS gmail
          ([user_id] INTEGER PRIMARY KEY, [user_name] TEXT, [gmail] TEXT, [phone] TEXT, [social_security] TEXT)
          ''')

conn.commit()


def print_database():
    c.execute("SELECT * FROM user_information")
    data = c.fetchall()
    print(data)


def pull_password(username):
    c.execute('SELECT password FROM user_information WHERE user_name = "' + username + '"')
    passwords = c.fetchall()
    return passwords[0][0]


def is_user(username):
    c.execute('SELECT user_name FROM user_information')
    users = c.fetchall()
    for user in users:
        if username == user[0]:
            return True
    return False


def pull_audio(username):
    c.execute('SELECT audioPreference FROM user_information WHERE user_name = "' + username + '"')
    audiopreference = c.fetchall()
    return audiopreference[0][0]
