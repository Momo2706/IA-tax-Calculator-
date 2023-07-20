import sqlite3

def insert_to_db(Name, Username, Password):
    conn1 = sqlite3.connect('my_app.db')
    passw = Password 
    conn1.execute(" INSERT INTO LOG_INFO (NAME, USER_NAME, PASSWORD) \
                 VALUES (?, ?, ?)", (Name, Username, passw))
    conn1.commit()
    conn1.close()

def validate_from_db(Name1, Username1, Password):
    conn2 = sqlite3.connect('my_app.db')
    passw1 = Password
    pword = conn2.execute(" SELECT PASSWORD from LOG_INFO where NAME = ? AND USER_NAME = ?", (Name1, Username1)).fetchone()
    val = False
    if pword[0] == passw1:
        val = True
        return val
    elif pword[0] != passw1:
        val = False 
        return val 
