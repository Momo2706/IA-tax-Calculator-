import sqlite3
from sqlite3 import Error
from model.country import Country
from typing import List

def get_countries() -> List[str]:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute("SELECT name FROM country").fetchall()
        country_names = [country_name[0] for country_name in result]
        return country_names
    except Error as e:
        print(e)

def get_phone_codes() -> List[str]:
    try:
        conn = sqlite3.connect('my_app.db')
        codes = conn.execute(" SELECT DISTINCT phone_code FROM country").fetchall()
        return codes
    except Error as e:
        print(e)

def get_currency() -> List[str]:
    try:
        conn = sqlite3.connect('my_app.db')
        money = conn.execute(" SELECT DISTINCT currency FROM country").fetchall()
        return money
    except Error as e:
        print(e)

def get_country_by_id(country_id: int) -> Country:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute(" SELECT name, phone_code FROM country WHERE id = ?", (country_id,)).fetchone()

        country = Country(name=result[0], phone_code=result[1][0])

        return country
    except Error as e:
        print(e)


def get_country_by_name(country: str) -> Country:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute(" SELECT name, phone_code FROM country WHERE name = ?", (country,)).fetchone()

        country = Country(name=result[0],phone_code=result[1])

        return country
    except Error as e:
        print(e)

def save_country(country: str, phone_code: str) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("INSERT INTO country (name, tax_border, phone_code) \
                 VALUES (?, ?)", (country, phone_code))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

def set_country_by_id(country_id: int, country: Country) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE country SET name = ? tax_border = ? WHERE id = ?", (
            country.name,
            country.tax_border,
            country_id
            ))
    except Error as e:
        print(e)
    return

def remove_country_by_id(country_id: int) -> Country:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("DELETE FROM country WHERE id = ?", (country_id))
    except Error as e:
        print(e)
    return