import sqlite3
from sqlite3 import Error
from model.country import Country

def get_country_by_id(country_id: int) -> Country:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, tax_border FROM country WHERE id = ?", (country_id)).fetchone()

    country = Country(name=result[0], tax_border=result[1])

    return country


def get_country_by_name(country: str) -> Country:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, tax_border FROM country WHERE country = ?", (country)).fetchone()

    country = Country(name=result[0], tax_border=result[1])

    return country

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
    conn = sqlite3.connect('my_app.db')
    conn.execute("DELETE FROM country WHERE id = ?")
    