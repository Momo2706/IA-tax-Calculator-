import sqlite3
from sqlite3 import Error
from model.bracket import Bracket 

def get_bracket_by_id(bracket_id: int) -> Bracket:
    conn = sqlite3.connect('my_app.db')
    results = conn.execute("SELECT lower_bound, upper_bound, percentage FROM bracket WHERE id = ?", (bracket_id)).fetchone()

    bracket = Bracket(lower_bound=results[0], upper_bound=results[1], percentage=results[2])

    return bracket

def get_bracket_by_country_id(country_id: int) -> Bracket:
    conn = sqlite3.connect('my_app.db')
    results = conn.execute("SELECT lower_bound, upper_bound, percentage FROM bracket WHERE country_id = ?", (country_id)).fetchone()

    bracket = Bracket(lower_bound=results[0], upper_bound=results[1], percentage=results[2])

    return bracket 

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

def remove_bracket_by_id(bracker_id: int) -> Bracket:
        conn = sqlite3.connect('my_app.db')
        conn.execute("DELETE FROM bracket WHERE id = ?")

        