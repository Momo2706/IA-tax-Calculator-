import PySimpleGUI as sg
import hashlib
from db.user_service import save_user
from ui.router import go_to
from db.country_service import get_countries, get_phone_codes, get_currency
from ui.menu import first_main_menu
from globals import session

sg.theme("DarkBlack1")

SIGNUP_WINDOW = [
        [sg.Text('Name'), sg.Input(key='-NAME-')],
        [sg.Text("Lastname(s): "), sg.InputText(key='-LASTNAME-', do_not_clear=True, size=(29,1))],
        [sg.Text('Username'), sg.Input(key='-USNAME-')],
        [sg.Text('Password'), sg.Input(key='-PASS-', password_char='*')],
        [sg.Text('Re-enter Password'), sg.Input(key='-REPASS-', password_char='*')],
        [sg.Text("Email:"), sg.InputText(key='-EMAIL-', do_not_clear=True, size=(35,1))],
        [sg.Text("Phone Number: "), sg.InputOptionMenu(values=get_phone_codes(), key='-PHONE_CODE-'), sg.InputText(key='-PHONE-', do_not_clear=True, size=(19,1))],
        [sg.Text("Marital status:")],
        [sg.Radio("Married", "PART", False, key='-MAR-'), sg.Radio("Divorced", "PART", False, key='-DIV-'), sg.Radio("Unwed", "PART", False, key='-UNMAR-')],
        [sg.Text("How many children do you have:")],
        [sg.Spin(values=[i for i in range(1000)], initial_value=0, size=(20, 2), enable_events=True, key='-KID-')],
        [sg.Text("What is your salary?"), sg.Input(key='-SALARY-', do_not_clear=True), sg.InputOptionMenu(values=get_currency(), key='-CASH-')],
        [sg.Text("Country of Residence"), sg.InputOptionMenu(values=get_countries(), key='-PLACE-')],
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
            last_name = values['-LASTNAME-']
            user = values['-USNAME-']
            email = values['-EMAIL-']
            phone_code = values['-PHONE_CODE-']
            phone_number = values['-PHONE-']
            kids = values['-KID-']
            salary = int(values['-SALARY-'])
            currency = values['-CASH-']
            country = values['-PLACE-']
            if pass1 == pass2:
                save_user(name, last_name, user, hashlib.md5(pass1.encode()).digest(), email, phone_code, phone_number, kids, salary, currency, country)
                session.set_user(user)
                go_to(signwindow, first_main_menu) # go to main menu
            else:
                signwindow.close()
                sg.popup('your passwords didnt match')
                go_to_signup()

    signwindow.close()