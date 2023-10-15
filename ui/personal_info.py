import PySimpleGUI as sg  
from ui.router import go_to
from db.country_service import get_phone_codes, get_countries
from db.history_service import set_history
from ui.confirmation import confirm_personal_info_changes_successful, confirm_tax_filling
from datetime import datetime
from model.income_tax import IncomeTax
from globals import session


def place_of_residence(residence):
               if residence == None:
                    return session.get_country
               else:
                    session.change_country(residence)
                    return session.get_country

sg.theme("DarkBlack1")

layout = [[sg.Text("Name:"), sg.InputText(key='-NAME-', do_not_clear=True, size=(35,1))],
          [sg.Text("Lastname(s): "), sg.InputText(key='-LASTNAME-', do_not_clear=True, size=(29,1))],
          [sg.Text("Email:"), sg.InputText(key='-EMAIL-', do_not_clear=True, size=(35,1))],
          [sg.Text("Phone Number: "), sg.Listbox(values=get_phone_codes(), select_mode="single", key='-COUNTRY-'), sg.InputText(key='-PHONE-', do_not_clear=True, size=(19,1))],
          [sg.Text("Marital status:")],
          [sg.Radio("Married", "PART", False, key='-MAR-'), sg.Radio("Divorced", "PART", False, key='-DIV-'), sg.Radio("Unwed", "PART", False, key='-UNMAR-')],
          [sg.Text("How many children do you have:")],
          [sg.Spin(values=[i for i in range(1000)], initial_value=0, size=(20, 2), enable_events=True, key='-KID-')],
          [sg.Submit(), sg.Cancel()]
]

def go_to_personal_info():
     sg.theme("DarkBlack1")
     person_window = sg.Window('info', layout)
     while True:
            event, _ = person_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break   
            elif event == 'Submit':
                go_to(person_window, confirm_personal_info_changes_successful)
     person_window.close()

def go_to_tax_info():
     sg.theme("DarkBlack1")
     layout = [[sg.Text("Where are you currently living?(if place of residence hasnt change do not select any country)")],
          [sg.InputOptionMenu(values=get_countries(), key='-COUNT-')],
          [sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Housing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("Set the date of when the tax is beeing filled"),sg.Input(key='-PICKUP-', size=(20, 1)), sg.CalendarButton("Filing Date", close_when_date_chosen=True, target='-PICKUP-', location=(0, 0), no_titlebar=False, format=('%Y-%m-%d'))],
          [sg.Submit(), sg.Button("Back"), sg.Cancel()]
        ]
     
     Window = sg.Window('tax Info', layout)
     
     while True:
          event, values = Window.read()
          if event == sg.WINDOW_CLOSED or event == 'Cancel':
               Window.close()
               break 
          if event == 'Submit':
               date_str = values['-PICKUP-']
               date = datetime.strptime(date_str, '%Y-%m-%d')
               salary = session.get_salary
               user = session.get_user
               country = place_of_residence(values['-COUNT-'])  
               tax_amount = IncomeTax.calculate_tax(salary, country)  
               amount_left = salary - tax_amount
               set_history(user, int(date), tax_amount, amount_left)
               go_to(Window, confirm_tax_filling)
               pass
          Window.close()
