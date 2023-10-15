import PySimpleGUI as sg
import hashlib
from db.user_service import log_in_user
from ui.menu import main_menu
from ui.router import go_to
from globals import session
#from ui.welcome import go_to_welcome

sg.theme("DarkBlack1")

LOGIN_WINDOW = [
        [sg.Text('Username'), sg.Input(key='-USNAME-')],
        [sg.Text('Password'), sg.Input(key='-PASS-', password_char='*')],
        [sg.Button('Login'), sg.Button('Cancel')]
    ]

def go_to_login():
    sg.theme("DarkBlack1")
    logwindow = sg.Window('Login Page', LOGIN_WINDOW)
    while True:
        event, values = logwindow.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            #go_to(logwindow, go_to_welcome)
            break

        if event == 'Login':
            user = values['-USNAME-']
            password = hashlib.md5(values['-PASS-'].encode()).digest()

            user = log_in_user(user, password)
            if user != None:
                session.set_user(user)
                go_to(logwindow, main_menu) # go to main menu
            else: 
                logwindow.close()
                sg.popup('Invalid username or password')
                go_to_login()

    logwindow.close()