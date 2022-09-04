import sqlite3


def connect(db):
    return sqlite3.connect(db)


def insert_sql(vcon, vsql):
    connection = vcon
    connection.cursor()
    connection.execute(vsql)
    connection.commit()


def select(vcon, user, passcode):
    connection = vcon.cursor()
    connection.execute(f'SELECT nome, sobrenome FROM UserData WHERE nome={user} and senha={passcode}')
    res = connection.fetchall()
    return res
