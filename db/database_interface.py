import sqlite3
from typing import List

def save_user(name, user, password, salary, country):
    conn = sqlite3.connect('my_app.db')
    country_id = conn.execute("SELECT id FROM country WHERE name = ?", (country)).fetchone()
    conn.execute(" INSERT INTO user (name, username, password, salary, country_id) \
                 VALUES (?, ?, ?)", (name, user, password, salary, country_id))
    conn.commit()
    conn.close()

def save_salary(salary, username, country, lower_bound, upper_bound):
    conn = sqlite3.connect('my_app.db')
    country_id = conn.execute("SELECT id FROM country WHERE name = ?", (country)).fetchone()
    bracket_id = conn.execute("SELECT id FROM bracket WHERE country_id = ?, lower_bound = ?, upper_bound = ?", (country_id, lower_bound, upper_bound)).fetchone()
    conn.execute("INSERT INTO user (salary, bracket_id) \
                 values(?, ?) WHERE username = ?", (salary, bracket_id, username))
    conn.commit()
    conn.close

# get_countries()
def country_list() -> List[str]:
    conn = sqlite3.connect('my_app.db')
    countries = conn.execute(" SELECT name FROM country").fetchall()
    return countries

# save_country
def adding_countries(country: str, tax_border: str) -> None:
    conn = sqlite3.connect('my_app.db')
    conn.execute("INSERT INTO country (name, tax_border) \
                 VALUES (?, ?)", (country, tax_border))
    conn.commit()
    conn.close()

def save_info_to_bracket(country, lower_bound, upper_bound, percentage):
    conn = sqlite3.connect('my_app.db')
    country_id = conn.execute("SELECT id FROM country WHERE name = ?", (country)).fetchone()
    conn.execute("INSERT INTO bracket (country_id, lower_bound, upper_bound, percentage) \
                 VALUES (?, ?, ?, ?)", (country_id, lower_bound, upper_bound, percentage))
    conn.commit()
    conn.close

