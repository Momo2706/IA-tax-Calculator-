import sqlite3
from sqlite3 import Error
from model.country import Country
from typing import List

#Returns a list of all the countries by name in the database 
def get_countries() -> List[str]:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute("SELECT name FROM country").fetchall()
        country_names = [country_name[0] for country_name in result]
        return country_names
    except Error as e:
        print(e)

#returns a list of all the distict phone codes in the database 
def get_phone_codes() -> List[str]:
    try:
        conn = sqlite3.connect('my_app.db')
        codes = conn.execute(" SELECT DISTINCT phone_code FROM country").fetchall()
        return codes
    except Error as e:
        print(e)

#returns a list of all the distinct currencies of the countries in the database 
def get_currency() -> List[str]:
    try:
        conn = sqlite3.connect('my_app.db')
        money = conn.execute(" SELECT DISTINCT currency FROM country").fetchall()
        return money
    except Error as e:
        print(e)

#returns a specific country and phone code by using the country id found in the table user 
def get_country_by_id(country_id: int) -> Country:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute(" SELECT id, name, phone_code FROM country WHERE id = ?", (country_id,)).fetchone()

        country = Country(id=result[0], name=result[1], phone_code=result[2][0])

        return country
    except Error as e:
        print(e)

#returns a specific country and phone code by using the name of the country
def get_country_by_name(country: str) -> Country:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute(" SELECT id, name, phone_code FROM country WHERE name = ?", (country,)).fetchone()

        country = Country(id=result[0], name=result[1], phone_code=result[2][0])

        return country
    except Error as e:
        print(e)

#allows for a new country to be inserted into the database if needed 
def save_country(country: str, phone_code: str) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("INSERT INTO country (name, phone_code) \
                 VALUES (?, ?)", (country, phone_code))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

#allows an update to be made in the case that a change in the country is made 
def set_country_by_id(country_id: int, country: Country) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE country SET name = ? phone_code WHERE id = ?", (
            country.name,
            country.phone_code,
            country_id
            ))
    except Error as e:
        print(e)
    return

#alows for a country row to be deleted from a database 
def remove_country_by_id(country_id: int) -> Country:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("DELETE FROM country WHERE id = ?", (country_id))
    except Error as e:
        print(e)
    return