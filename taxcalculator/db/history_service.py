import sqlite3
from taxcalculator.model.user import User
from sqlite3 import Error 
from taxcalculator.model.history import History
from typing import List

#after the tax has been calculated the user date and tax paid are saved into the database 
def set_history(user: User, date, tax_paid):
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("INSERT INTO history (user_id, date, tax_amount) \
                    VALUES(?, ?, ?)", (user.id, date, tax_paid))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

#retrieves the users acording to a specific date 
def get_users_from_date(date: str) -> History:
    try:
        conn = sqlite3.connect('my_app.db')
        users = conn.execute("SELECT user_name FROM history WHERE date = ?", (date,)).fetchall()
        return users
    except Error as e:
        print(e)

#returns the amount of tax paid per date by a certain user 
def get_tax_paid_from_user(user_id: int) -> History:
    try:
        conn = sqlite3.connect('my_app.db')
        tax_paid = conn.execute("SELECT tax_amount, date FROM history WHERE user_id = ?", (user_id,)).fetchall()
        return tax_paid
    except Error as e:
        print(e)

#returns a specific tax amount in accordance to a user and a date 
def get_tax_paid_form_user_and_date(user_id: int, date: str) -> History:
    try:
        conn = sqlite3.connect('my_app.db')
        tax_paid = conn.execute("SELECT tax_amount FROM history WHERE user_id = ? AND date = ?", (user_id, date)).fetchone()
        return tax_paid
    except Error as e:
        print(e)

#updates the taxes in a date if needed 
def set_tax_paid_by_date_and_user(user_id: int, date: str, history: History) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE history SET tax_amount = ? WHERE user_id = ? AND date = ?", 
                           (
                            history.tax_amount,
                            user_id, 
                            date
                           ))
    except Error as e:
        print(e)
    return

#deletes a piece of history from the database
def delete_history_by_id(id: int) -> History:
        try:
            conn = sqlite3.connect('my_app.db')
            conn.execute("DELETE FROM history WHERE id = ?", (id))
        except Error as e:
             print(e)
        return

#retrives all data in history for a specific user
def get_history_by_user(user: User) -> List[History]:
    try:
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
    except Error as e:
        print(e)