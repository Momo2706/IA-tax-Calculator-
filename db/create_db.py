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
         bracket_id INTEGER NOT NULL,
         FOREIGN KEY(bracket_id) REFERENCES bracket(id)
         )
         '''
        )
query2 = ('''
         CREATE TABLE country
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         tax_border TEXT NOT NULL
         )
        '''
        )
query3 = ('''
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

# create history

conn.execute(query)
conn.execute(query2)
conn.execute(query3)
conn.execute("INSERT INTO country (name, tax_border) \
              VALUES (?, ?)", ("United States of America", "Citizen Based"))
conn.commit()
conn.close()
