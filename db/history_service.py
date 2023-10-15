import sqlite3
from sqlite3 import Error 
from model.history import History
from typing import List


def set_history(user, date, tax_paid, amount_left):
    conn = sqlite3.connect('my_app.db')
    user_id = conn.execute("SELECT id FROM user WHERE username = ?", (user,)).fetchone()
    conn.execute("INSERT INTO history (user_id, date, tax_amount, amount_left) \
                 VALUES(?, ?, ?, ?)", (user_id, date, tax_paid, amount_left))

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
                            history.amount_left,
                            user_id, 
                            date
                           ))
    except Error as e:
        print(e)
    return

def remove_tax_paid_by_date_and_user(user_id: int, date: str) -> History:
        try:
            conn = sqlite3.connect('my_app.db')
            conn.execute("DELETE FROM bracket WHERE user_id = ? AND date = ?", (user_id, date))
        except Error as e:
             print(e)
        return

def get_dates_and_amount_by_user(user: str) -> List[History]:
    conn = sqlite3.connect('my_app.db')

    history: List[History] = []

    results = conn.execute('''
                        SELECT history.date, history.tax_amount, history.amount_left
                        FROM history
                        LEFT JOIN user ON user.id = history.user_id
                        WHERE user.username = ?
                        ORDER BY history.date ASC
                        ''', (user,)).fetchall()
    for history in results:
        history.append(History(date=history[0], tax_amount=history[1], amount_left=history[2]))

    return history 