import sqlite3
conn = sqlite3.connect('my_app.db')

query = (''' 
         CREATE TABLE user
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         username TEXT NOT NULL, 
         password TEXT NOT NULL,
         salary INTEGER NOT NULL,
         country_id INTEGER NOT NULL,
         FOREIGN KEY(country_id) REFERENCES country(id)
         )
         '''
        )
conn.execute(query)

query = ('''
         CREATE TABLE country
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         tax_border TEXT NOT NULL,
         phone_code TEXT NOT NULL
         )
        '''
        )
conn.execute(query)

query = ('''
         CREATE TABLE bracket
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         country_id INTEGER NOT NULL,
         lower_bound INTEGER NOT NULL,
         upper_bound INTEGER NOT NULL,
         percentage INTEGER NOT NULL,
         FOREIGN KEY(country_id) REFERENCES country(id)
         )
        '''
        )
conn.execute(query)

query = ('''
        CREATE TABLE history
        (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         user_id INTEGERN NOT NULL,
         date TEXT NOT NULL, 
         tax_amount INTEGER NOT NULL, 
         amount_left INTEGER NOT NULL, 
         FOREIGN KEY(user_id) REFERENCES user(id)
        )
        '''
         )

#add already 10-15 countries and their respective tax boarders

conn.execute(query)
conn.commit()
conn.close()
