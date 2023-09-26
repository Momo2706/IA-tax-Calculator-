import sqlite3
from sqlite3 import Error 
from model.history import History

def get_users_from_date(date: str) -> History:
    conn = sqlite3.connect('my_app.db')
    users = conn.execute("SELECT user_name FROM history WHERE date = ?", (date)).fetchall()
    return users

def get_tax_paid_from_user(user_id: int) -> History:
    conn = sqlite3.connect('my_app.db')
    tax_paid = conn.execute("SELECT tax_amount, date FROM history WHERE user_id = ?", (user_id)).fetchall()
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

