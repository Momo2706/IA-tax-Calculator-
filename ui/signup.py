import PySimpleGUI as sg
import hashlib
from personal_info import personal_info
from db.database_interface import insert_to_db, validate_from_db
from my_app_functions import tax

SIGNUP_WINDOW = [
        [sg.Text('Name'), sg.Input(key='-NAME-')],
        [sg.Text('Username'), sg.Input(key='-USNAME-')],
        [sg.Text('Password'), sg.Input(key='-PASS-', password_char='*')],
        [sg.Text('Re-enter Password'), sg.Input(key='-REPASS-', password_char='*')],
        [sg.Button('sign_up'), sg.Button('Cancel')]
    ]

def go_to_signup():
    
    signwindow = sg.Window('Signup page', SIGNUP_WINDOW)
    while True:
        event, values = signwindow.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == 'sign_up':
            pass1 = values['-PASS-']
            pass2 = values['-REPASS-']
            name = values['-NAME-']
            user = values['-USNAME-']
            if pass1 == pass2:
                insert_to_db(name, user, hashlib.md5(pass1.encode()).digest())
                signwindow.close()
                personal_info()
            else:
                signwindow.close()
                sg.popup('your passwords didnt match')
                go_to_signup()

    signwindow.close()