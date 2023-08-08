import sqlite3


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
         country_id INTEGER NOT NULL

         FOREIGN KEY(country_id) REFERENCES country(id)
         );

         CREATE TABLE country
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         tax_border TEXT NOT NULL
         );

         CREATE TABLE bracket
         (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         country_id INTEGER NOT NULL,
         lower_bound INTEGER NOT NULL,
         upper_bound INTEGER NOT NULL,
         percentage INTEGER NOT NULL

         FOREIGN KEY(country_id) REFERENCES country(id)
         )
         '''

         # Past results
)

conn.execute(query)
conn.close()

# conn = sqlite3.connect('my_app.db')
# conn.execute("INSERT INTO country_tax (country, country_code, tax_borders, min_taxable_income) \
#              VALUES (?, ?, ?, ?)", ("United States of America", "+1", "Citizen Based", 12950))
# conn.commit()
# conn.close()
