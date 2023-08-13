import sqlite3
from sqlite3 import Error
from model.user import User

def get_user(user_id: int) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE id = ?", (user_id)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

def get_user_by_username(username: str) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE username = ?", (username)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

def get_salary_by_user(user_id: int) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute("SELECT name, salary FROM user WHERE id = ?", (user_id)).fetchone()

    user = User(name=result[0], salary=result[1])

    return user

def set_salary_by_id(user_id: int, user: User) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("UPDATE user SER salary = ? WHERE id = ?",
                     (
                        user.salary,
                        user_id
                     )
                     )
    except Error as e:
        print(e)
    return

def remove_user_by_id(user_id: int) -> User:
    conn = sqlite3.connect('my_app.db')
    conn.execute("DELETE FROM user WHERE id = ?")
    
