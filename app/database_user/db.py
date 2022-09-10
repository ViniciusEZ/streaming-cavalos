import sqlite3


def connect(db):
    return sqlite3.connect(db)


def insert_sql(vcon, values):
    connection = vcon
    connection.cursor()
    connection.execute(f'INSERT INTO UserData VALUES (?,?,?,?,?,?,?,?,?,?,?)', tuple([value for value in values]))
    connection.commit()


def select(vcon, user, passcode):
    connection = vcon.cursor()
    connection.execute(f'SELECT nome, sobrenome FROM UserData WHERE usuario=? and senha=?', (user, passcode))
    res = connection.fetchall()
    return res


