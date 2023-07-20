import sqlite3

conn = sqlite3.connect('my_app.db')
query = (''' CREATE TABLE LOG_INFO
         (NAME TEXT NOT NULL,
         USER_NAME TEXT NOT NULL, 
         PASSWORD TEXT NOT NULL);'''
         )
conn.execute(query)
conn.close() 