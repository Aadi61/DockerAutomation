import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Containers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, port INTEGER)')
cursor.close()

def insert_container(name, port):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Containers (name, port) VALUES (?, ?)', (name, port))
    connection.commit()

def check_port(port):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Containers WHERE port=?', (port,))
    return cursor.fetchone()

def remove_container(port):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Containers WHERE port=?', (port,))
    connection.commit()
