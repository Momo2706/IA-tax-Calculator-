import PySimpleGUI as sg
import hashlib
from taxcalculator.db.user_service import save_user, log_in_user, check_if_username_is_used
from taxcalculator.ui.router import go_to
from taxcalculator.db.country_service import get_countries, get_phone_codes, get_currency
from taxcalculator.ui.menu import first_main_menu
from taxcalculator.globals import session

def go_to_signup():
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
            username = values['-USNAME-']
            email = values['-EMAIL-']
            phone_number = values['-PHONE-']
            kids = values['-KID-'] 
            salary = int(values['-SALARY-'])
            currency = values['-CASH-'] 
            country = values['-PLACE-']

            is_error = False

            #checks that all posible variables have been answered or filled in to get the most accurate results
            for key, value in values.items():
                if value == '':
                    is_error = True
                    error_window = sg.Window('Error', [
                        [sg.Text(f"Field {key} cannot be empty")],
                        [sg.Button('Accept')]
                    ])
                    error_event, _ = error_window.read()
                    if error_event == sg.WINDOW_CLOSED or error_event == 'Accept':
                        error_window.close()
                        break
            
            if is_error:
                continue

            is_user_used = check_if_username_is_used(username)
            if pass1 == pass2 and is_user_used == False:
                save_user(name, last_name, username, hashlib.md5(pass1.encode()).digest(), email, phone_number, kids, salary, currency, country)
                user = log_in_user(username, hashlib.md5(pass1.encode()).digest())
                session.set_user(user)
                go_to(signwindow, first_main_menu)
            else:
                signwindow.close()
                sg.popup('your passwords didnt match or username is already  in use')
                go_to_signup()

    signwindow.close()