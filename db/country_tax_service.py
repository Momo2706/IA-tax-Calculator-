
import sqlite3
from sqlite3 import Error
from model.country_tax import Country

def get_country_tax_by_id(country_id: int) -> Country:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, tax_border FROM country WHERE id = ?", (country_id)).fetchone()

    country_tax = Country(name=result[0], tax_border=result[1])

    return country_tax


def get_country_tax_by_country(country: str) -> Country:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, tax_border FROM country WHERE country = ?", (country)).fetchone()

    country_tax = Country(name=result[0], tax_border=result[1])

    return country_tax

def set_country_tax_by_id(country_id: int, country_tax: Country) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE country SET name = ? tax_border = ? WHERE id = ?", (
            country_tax.name,
            country_tax.tax_border,
            country_id
            ))
    except Error as e:
        print(e)
    return