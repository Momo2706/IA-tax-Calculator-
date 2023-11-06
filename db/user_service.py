import sqlite3
from sqlite3 import Error
from model.user import User
from model.country import Country
from db.country_service import get_country_by_id

#returns user from database in accordance to their user id 
def get_user(user_id: int) -> User:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute(" SELECT name, user FROM user WHERE id = ?", (user_id,)).fetchone()

        user = User(name=result[0], username=result[1])

        return user
    except Error as e:
        print(e)


# authenticate_user and set object from class user 
def log_in_user(username, password) -> User:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute("SELECT id, name, last_name, username, password, email, phone_number, kids, salary, currency, country_id FROM user WHERE username = ?", (username,)).fetchone()
        
        if result == None:
            return None

        if result[4] != password:
            return None

        country = get_country_by_id(int(result[10]))

        user = User(id=result[0], name=result[1], last_name=result[2], username=result[3], password=result[4], email=result[5], phone_number=result[6], kids=result[7], salary=result[8], currency=result[9][0], country=country)

        return user
    except Error as e:
        print(e)

#returns name and username from database 
def get_user_by_username(username: str) -> User:
    try:
        conn = sqlite3.connect('my_app.db')
        result = conn.execute(" SELECT name, username FROM user WHERE username = ?", (username,)).fetchone()

        user = User(name=result[0], username=result[1])

        return user
    except Error as e:
        print(e)


#updates the table user in the databse if needed 
def update_user(user: User) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("""
            UPDATE user
            SET name = ?, 
                last_name = ?, 
                username = ?, 
                email = ?, 
                phone_number = ?, 
                kids = ?, 
                salary = ?, 
                currency = ?, 
                country_id = ?
            WHERE id = ?
        """,
        (user.name, user.last_name, user.username, user.email, user.phone_number, user.kids, user.salary, user.currency, user.country.id, user.id)
        )
        conn.commit()
        conn.close()

    except Error as e:
        print(e)


#deletas a row in the table user from the database if needed to 
def remove_user_by_id(user_id: int) -> None:
    try:
        conn = sqlite3.connect('my_app.db')
        conn.execute("DELETE FROM user WHERE id = ?", (user_id))
    except Error as e:
        print(e)

#saves the information of a person signing up to the database so it can later be used
def save_user(name, last_name, user, password, email, phone_number, kids, salary, currency, country):
    try:
        conn = sqlite3.connect('my_app.db')
        country_id = conn.execute("SELECT id FROM country WHERE name = ?", (country,)).fetchone()
        conn.execute("INSERT INTO user (name, last_name, username, password, email, phone_number, kids, salary, currency, country_id) \
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, last_name, user, password, email, phone_number, kids, salary, currency, country_id[0]))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

#to not cause confutions within the database this checks that no two usernames are alike
def check_if_username_is_used(username):
    try:
        conn = sqlite3.connect('my_app.db')
        user = conn.execute("SELECT username FROM user").fetchall()
        existance = False
        for i in range(len(user)):
            existance = False
            print(type(user[i][0]))
            print(user[i][0], username)
            if user[i][0] == username:
                existance = True
                break
        print(existance)
        return existance
    except Error as e:
        print(e)


