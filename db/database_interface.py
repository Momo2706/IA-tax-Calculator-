import sqlite3

#checks for the existance of the datbase when the code is first started
def is_db_connected():
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("SELECT * FROM history") 
        return True
    except sqlite3.OperationalError:
        return False