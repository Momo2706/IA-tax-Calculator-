import PySimpleGUI as sg 
import calendar 
from taxcalculator.ui.router import go_to
from typing import List
from taxcalculator.model.tax import Tax
from taxcalculator.db.country_service import get_countries, get_phone_codes, get_currency, get_country_by_name
from taxcalculator.db.history_service import set_history
from taxcalculator.db.user_service import update_user, log_in_user
from taxcalculator.ui.confirmation import confirm_personal_info_changes_successful, confirm_tax_filling
from datetime import datetime
from taxcalculator.model.income_tax import IncomeTax
from taxcalculator.model.property_tax import PropertyTax
from taxcalculator.globals import session

sg.theme("DarkBlack1")

def get_appliable_taxes() -> List[Tax]:
     user = session.get_user()
     appliable_taxes: List[Tax] = []
     #future application of more taxes
     appliable_taxes.append(IncomeTax())

def go_to_personal_info():
    user = session.get_user()
    PERSONAL_WINDOW = [
             [sg.Text('Name'), sg.Input(user.name, key='-NAME-')],
             [sg.Text("Lastname(s): "), sg.InputText(user.last_name, key='-LASTNAME-', do_not_clear=True, size=(29,1))],
             [sg.Text('Username'), sg.Input(user.username, key='-USNAME-')],
             [sg.Text("Email:"), sg.InputText(user.email, key='-EMAIL-', do_not_clear=True, size=(35,1))],
             [sg.Text("Phone Number: "), sg.InputOptionMenu(default_value=user.country.phone_code, values=get_phone_codes(), key='-PHONE_CODE-'), sg.InputText(user.phone_number, key='-PHONE-', do_not_clear=True, size=(19,1))],
             [sg.Text("Marital status:")],
             [sg.Radio("Married", "PART", False, key='-MAR-'), sg.Radio("Divorced", "PART", False, key='-DIV-'), sg.Radio("Unwed", "PART", False, key='-UNMAR-')],
             [sg.Text("How many children do you have:")],
             [sg.Spin(values=[i for i in range(1000)], initial_value=user.kids, size=(20, 2), enable_events=True, key='-KID-')],
             [sg.Text("What is your salary?"), sg.Input(user.salary, key='-SALARY-', do_not_clear=True), sg.InputOptionMenu(default_value=user.currency, values=get_currency(), key='-CASH-')],
             [sg.Text("Country of Residence"), sg.InputOptionMenu(default_value=user.country.name, values=get_countries(), key='-PLACE-')],
             [sg.Button('Submit'), sg.Button('Cancel')]
            ]
    sg.theme("DarkBlack1")
    person_window = sg.Window('Signup page', PERSONAL_WINDOW)
    while True:
        event, values = person_window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        user = session.get_user()
        user.name = values['-NAME-']
        user.username = values['-USNAME-']
        user.salary = int(values['-SALARY-'])
        country_name = values['-PLACE-']
        country = get_country_by_name(country_name)
        user.country = country
        user.last_name = values['-LASTNAME-']
        user.email = values['-EMAIL-']
        user.phone_number = values['-PHONE-']
        user.kids = values['-KID-']
        user.currency = values['-CASH-']
        if event == 'Submit':
                update_user(user=user)
                go_to(person_window, confirm_personal_info_changes_successful)
    person_window.close()

def go_to_tax_info():
     sg.theme("DarkBlack1")
     layout = [
          [sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Housing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("Set the date of when the tax is beeing filled"),sg.Input(key='-PICKUP-', size=(20, 1)), sg.CalendarButton("Filing Date", close_when_date_chosen=True, target='-PICKUP-', location=(0, 0), no_titlebar=False, format=('%Y'))],#for a full date = '%Y-%m-%d'
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
               date = datetime.strptime(date_str, '%Y')
               user = session.get_user()

               appliable_taxes = get_appliable_taxes()
               
               appliable_taxes: List[Tax] = [IncomeTax()]
               total_tax_amount = 0

               for tax in appliable_taxes:
                    total_tax_amount = total_tax_amount + tax.calculate_tax(user)
               
               set_history(user, calendar.timegm(date.timetuple()), total_tax_amount)
               go_to(Window, confirm_tax_filling)
               pass
          Window.close()
