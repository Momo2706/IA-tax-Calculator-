import sqlite3
from sqlite3 import Error
from model.bracket import Bracket 
from typing import List

#Retrieves the tax bracket according to their ID in the database
def get_bracket_by_id(bracket_id: int) -> Bracket:
    try:
        conn = sqlite3.connect('my_app.db')
        results = conn.execute("SELECT lower_bound, upper_bound, percentage FROM bracket WHERE id = ?", (bracket_id,)).fetchone()

        bracket = Bracket(lower_bound=results[0], upper_bound=results[1], percentage=results[2])

        return bracket
    except Error as e:
         print(e)

#retrieves the tax brackets of a country by using the countries name 
def get_brackets_by_country_name(name: str) -> List[Bracket]:
    try:
        conn = sqlite3.connect('my_app.db')

        brackets: List[Bracket] = []

        results = conn.execute('''
                            SELECT bracket.country_id, bracket.lower_bound, bracket.upper_bound, bracket.percentage
                            FROM bracket
                            LEFT JOIN country ON country.id = bracket.country_id
                            WHERE country.name = ?
                            ORDER BY bracket.lower_bound ASC
                            ''', (name,)).fetchall()
    
        for bracket in results:
            brackets.append(Bracket(country_id=bracket[0], lower_bound=bracket[1], upper_bound=bracket[2], percentage=bracket[3]))

        return brackets
    except Error as e:
         print(e)

#Updates the tax brackests according to the bracket id 
def set_bracket_by_id(bracket_id: int, bracket: Bracket) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE bracket SET lower_bound = ?, upper_bound = ?, percentage = ? WHERE id = ?", 
                           (
                            bracket.lower_bound,
                            bracket.upper_bound,
                            bracket.percentage,
                            bracket_id
                           ))
    except Error as e:
        print(e)
    return

#deletes brackest according to their bracket id
def delete_bracket_by_id(bracket_id: int) -> Bracket:
        try:
            conn = sqlite3.connect('my_app.db')
            conn.execute("DELETE FROM bracket WHERE id = ?", (bracket_id))
        except Error as e:
             print(e)
        return

        