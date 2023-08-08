import sqlite3

conn = sqlite3.connect('my_app.db')
conn.execute("INSERT INTO country_tax (country, country_code, tax_borders, min_taxable_income) \
             VALUES (?, ?, ?, ?)", ("United States of America", "+1", "Citizen Based", 12950))
conn.commit()
conn.close()
