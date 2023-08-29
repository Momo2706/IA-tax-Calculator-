import sqlite3
from typing import List

# save_user()
def insert_to_db(name, username, password):
    conn = sqlite3.connect('my_app.db')
    conn.execute(" INSERT INTO user (name, username, password) \
                 VALUES (?, ?, ?)", (name, username, password))
    conn.commit()
    conn.close()

# authenticate_user
def validate_from_db(name, username, password) -> bool:
    conn = sqlite3.connect('my_app.db')
    pword = conn.execute(" SELECT password FROM user WHERE name = ? AND username = ?", (name, username)).fetchone()
    
    return pword[0] == password

# get_countries()
def country_list() -> List[str]:
    conn = sqlite3.connect('my_app.db')
    countries = conn.execute(" SELECT name FROM country").fetchall()
    return countries

# save_country
def adding_countries(country: str, tax_border: str) -> None:
    conn = sqlite3.connect('my_app.db')
    conn.execute("INSERT INTO country (name, tax_borders) \
                 VALUES (?, ?)", (country, tax_border))
    conn.commit()
    conn.close()
