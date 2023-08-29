import PySimpleGUI as sg
import hashlib
from personal_info import personal_info
from db.database_interface import insert_to_db, validate_from_db
from my_app_functions import tax
from router import go_to
from welcome import go_to_welcome

LOGIN_WINDOW = [
        [sg.Text('Name'), sg.Input(key='-NAME-')],
        [sg.Text('Username'), sg.Input(key='-USNAME-')],
        [sg.Text('Password'), sg.Input(key='-PASS-', password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

def go_to_login():
    logwindow = sg.Window('Login Page', LOGIN_WINDOW)
    while True:
        event, values = logwindow.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'Login':
            name = values['-NAME-']
            user = values['-USNAME-']
            password = hashlib.md5(values['-PASS-'].encode()).digest()
            d = validate_from_db(name, user, password)
            if d == True:
                logwindow.close()
                tax()
            elif d == False: 
                logwindow.close()
                sg.popup('Invalid username or password')
                go_to_login()

    go_to(logwindow, go_to_welcome)
    logwindow.close()