import sqlite3
from model.user import User

def get_user(user_id: int) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE id = ?", (user_id)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

def get_user_by_username(username: int) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE username = ?", (username)).fetchone()

    user = User(name=result[0], username=result[1])

    return user