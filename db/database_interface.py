import sqlite3

def insert_to_db(name, username, password):
    conn = sqlite3.connect('my_app.db')
    conn.execute(" INSERT INTO user (name, username, password) \
                 VALUES (?, ?, ?)", (name, username, password))
    conn.commit()
    conn.close()

def validate_from_db(name1, username1, password):
    conn = sqlite3.connect('my_app.db')
    pword = conn.execute(" SELECT password FROM user WHERE name = ? AND username = ?", (name1, username1)).fetchone()
    val = False
    if pword[0] == password:
        val = True
        return val
    elif pword[0] != password:
        val = False 
        return val
