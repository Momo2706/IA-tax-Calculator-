import PySimpleGUI as sg
import hashlib
from ui.login import go_to_login
from db.user_service import save_user
from ui.router import go_to
from db.country_service import save_country 
from globals import session

sg.theme("DarkBlack1")

SIGNUP_WINDOW = [
        [sg.Text('Name'), sg.Input(key='-NAME-')],
        [sg.Text("Lastname(s): "), sg.InputText(key='-LASTNAME-', do_not_clear=True, size=(29,1))],
        [sg.Text('Username'), sg.Input(key='-USNAME-')],
        [sg.Text('Password'), sg.Input(key='-PASS-', password_char='*')],
        [sg.Text('Re-enter Password'), sg.Input(key='-REPASS-', password_char='*')],
        [sg.Text("Email:"), sg.InputText(key='-EMAIL-', do_not_clear=True, size=(35,1))],
        [sg.Text("Phone Number: "), sg.Listbox(values=['+1', '+31', '+34', '+44', '+377'], select_mode="single", key='-COUNTRY-'), sg.InputText(key='-PHONE-', do_not_clear=True, size=(19,1))],
        [sg.Text("Marital status:")],
        [sg.Radio("Married", "PART", False, key='-MAR-'), sg.Radio("Divorced", "PART", False, key='-DIV-'), sg.Radio("Unwed", "PART", False, key='-UNMAR-')],
        [sg.Text("How many children do you have:")],
        [sg.Spin(values=[i for i in range(1000)], initial_value=0, size=(20, 2), enable_events=True, key='-KID-')],
        [sg.Text("What is your salary?"), sg.InputText(key='-Salary-', do_not_clear=True)],
        [sg.Text("Country of Residance"), sg.Input(key='-PLACE-')],
        [sg.Text("Tax Borders")],
        [sg.InputOptionMenu(values=["Citizen Based", "Resident Based", "Territorial Based"], key='-BOR-')],
        [sg.Button('sign_up'), sg.Button('Cancel')]
    ]

def go_to_signup():
    sg.theme("DarkBlack1")
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
            salary = values['-Salary-']
            country = values['-PLACE-']
            border = values['-BOR-'] 
            save_country(country, border)
            if pass1 == pass2:
                save_user(name, user, hashlib.md5(pass1.encode()).digest(), salary, country)
                session.set_user(user)
                go_to(signwindow, go_to_login) # go to main menu
            else:
                signwindow.close()
                sg.popup('your passwords didnt match')
                go_to_signup()

    signwindow.close()