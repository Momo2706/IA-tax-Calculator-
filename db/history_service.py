import sqlite3
from model.user import User
from sqlite3 import Error 
from model.history import History
from typing import List


def set_history(user: User, date, tax_paid):
    conn = sqlite3.connect('my_app.db')
    try:
        conn.execute("INSERT INTO history (user_id, date, tax_amount) \
                    VALUES(?, ?, ?)", (user.id, date, tax_paid))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

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

def get_history_by_user(user: User) -> List[History]:
    conn = sqlite3.connect('my_app.db')

    assert user != None

    histories: List[History] = []

    results = conn.execute('''
                        SELECT history.date, history.tax_amount
                        FROM history
                        LEFT JOIN user ON user.id = history.user_id
                        WHERE user.username = ?
                        ORDER BY history.date ASC
                        ''', (user.username,)).fetchall()
    for history in results:
        histories.append(History(user=user, date=history[0], tax_amount=history[1]))

    return histories