import sqlite3
from sqlite3 import Error
from model.user import User
from db.country_service import get_country_by_id

def get_user(user_id: int) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE id = ?", (user_id,)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

# authenticate_user
def log_in_user(username, password) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute("SELECT id, name, last_name, username, password, email, phone_code, phone_number, kids, salary, currency, country_id FROM user WHERE username = ?", (username,)).fetchone()

    if result[4] != password:
        return None
    
    contries = get_country_by_id(int(result[11]))
    
    user = User(name=result[1], last_name=result[2], username=result[3], password=result[4], email=result[5], phone_code=result[6], phone_number=result[7], kids=result[8], salary=result[9], currency=result[10], country=contries.name)

    return user

def get_user_by_username(username: str) -> User:
    conn = sqlite3.connect('my_app.db')
    result = conn.execute(" SELECT name, user FROM user WHERE username = ?", (username,)).fetchone()

    user = User(name=result[0], username=result[1])

    return user

#finish this correctly
def update_user(og_name, name, last_name, username, password, email, phone_code, phone_number, kids, salary, currency, country) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        id = conn.execute("SELECT id FROM user WHERE name = ?", (og_name,)).fetchone()
        country_id = conn.execute("SELECT id FROM country WHERE name = ?", (country,)).fetchone()
        conn.execute("UPDATE user SET name = ? last_name = ? username = ? password = ? email = ? phone_code = ? phone_number = ? kids = ? salary = ? currency = ? country_id = ? WHERE id = ?", (name, last_name, username, password, email, phone_code, phone_number, kids, salary, currency, country_id, id))
    except Error as e:
        print(e)
    return


def remove_user_by_id(user_id: int) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("DELETE FROM user WHERE id = ?", (user_id))
    except Error as e:
        print(e)
    return

def save_user(name, last_name, user, password, email, phone_code, phone_number, kids, salary, currency, country):
    conn = sqlite3.connect('my_app.db')
    country_id = conn.execute("SELECT id FROM country WHERE name = ?", (country,)).fetchone()
    conn.execute("INSERT INTO user (name, last_name, username, password, email, phone_code, phone_number, kids, salary, currency, country_id) \
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, last_name, user, password, email, phone_code, phone_number, kids, salary, currency, country_id[0]))
    conn.commit()
    conn.close()


