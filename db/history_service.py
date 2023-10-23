import sqlite3
from sqlite3 import Error 
from model.history import History
from typing import List


def set_history(user, date, tax_paid):
    conn = sqlite3.connect('my_app.db')
    user_id = conn.execute("SELECT id FROM user WHERE username = ?", (user,)).fetchone()
    conn.execute("INSERT INTO history (user_id, date, tax_amount) \
                 VALUES(?, ?, ?)", (user_id[0], date, tax_paid))
    print("history set")

def get_users_from_date(date: str) -> History:
    conn = sqlite3.connect('my_app.db')
    users = conn.execute("SELECT user_name FROM history WHERE date = ?", (date,)).fetchall()
    return users

def get_tax_paid_from_user(user_id: int) -> History:
    conn = sqlite3.connect('my_app.db')
    tax_paid = conn.execute("SELECT tax_amount, date FROM history WHERE user_id = ?", (user_id,)).fetchall()
    return tax_paid

def get_tax_paid_form_user_and_date(user_id: int, date: str) -> History:
    conn = sqlite3.connect('my_app.db')
    tax_paid = conn.execute("SELECT tax_amount FROM history WHERE user_id = ? AND date = ?", (user_id, date)).fetchone()
    return tax_paid

def set_tax_paid_by_date_and_user(user_id: int, date: str, history: History) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE history SET tax_amount = ?, amount_left = ? WHERE user_id = ? AND date = ?", 
                           (
                            history.tax_amount,
                            user_id, 
                            date
                           ))
    except Error as e:
        print(e)
    return

def delete_history_by_id(id: int) -> History:
        try:
            conn = sqlite3.connect('my_app.db')
            conn.execute("DELETE FROM history WHERE id = ?", (id))
        except Error as e:
             print(e)
        return

def get_history_by_user(user: str) -> List[History]:
    conn = sqlite3.connect('my_app.db')

    history: List[History] = []

    results = conn.execute('''
                        SELECT history.date, history.tax_amount
                        FROM history
                        LEFT JOIN user ON user.id = history.user_id
                        WHERE user.username = ?
                        ORDER BY history.date ASC
                        ''', (user,)).fetchall()
    for history in results:
        history.append(History(date=history[0], tax_amount=history[1]))

    return history 