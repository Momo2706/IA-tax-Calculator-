import sqlite3
from sqlite3 import Error
from model.user import User
from db.country_service import get_country_by_id

def get_user(user_id: int) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE id = ?", (user_id)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

# authenticate_user
def log_in_user(name, username, password) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT id, user, username, password, salary, country_id FROM user WHERE name = ? AND username = ?", (name, username)).fetchone()

    if result[3] != password:
        return None

    user = User(id=result[0], name=result[1], username=result[2], salary=result[4], country=get_country_by_id(int(result[5])))

    return user

def get_user_by_username(username: str) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE username = ?", (username)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

def remove_user_by_id(user_id: int) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("DELETE FROM user WHERE id = ?", (user_id))
    except Error as e:
        print(e)
    return

#def save_user(user: User):
    #conn = sqlite3.connect('my_app.db')
    #conn.execute(" INSERT INTO user (name, username, password, salary, country) \
                 #VALUES (?, ?, ?)", (user.name, user.username, user.password, user.salary, user.country))
    #conn.commit()
    #conn.close()
