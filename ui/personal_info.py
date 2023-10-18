import PySimpleGUI as sg 
import calendar 
from ui.router import go_to
from typing import List
from model.tax import Tax
from db.country_service import get_phone_codes, get_countries
from db.history_service import set_history
from ui.confirmation import confirm_personal_info_changes_successful, confirm_tax_filling
from datetime import datetime
from model.income_tax import IncomeTax
from model.property_tax import PropertyTax
from globals import session

sg.theme("DarkBlack1")

def get_appliable_taxes() -> List[Tax]:
     user = session.get_user()
     appliable_taxes: List[Tax] = []

     if user.country.name != "Monaco":
          appliable_taxes.append(IncomeTax())
     
     appliable_taxes.append(PropertyTax())

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
     layout = [
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
               user = session.get_user()

               #appliable_taxes = get_appliable_taxes()
               
               appliable_taxes: List[Tax] = [IncomeTax()]
               total_tax_amount = 0

               for tax in appliable_taxes:
                    total_tax_amount += tax.calculate_tax(user=user)
               
               set_history(user, calendar.timegm(date.timetuple()), total_tax_amount)
               go_to(Window, confirm_tax_filling)
               pass
          Window.close()
