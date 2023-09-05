from typing import List
import PySimpleGUI as sg
from model.tax import Tax
from model.income_tax import IncomeTax
from db.database_interface import country_list, adding_countries, save_salary, save_info_to_bracket
from ui.login import username, password


def add_country():
     sg.theme("DarkBlack1")
     editlayout = [[sg.Text("Country"), sg.Input(key='-PLACE-')],
                   [sg.Text("Tax Borders")],
                   [sg.InputOptionMenu(values=["Citizen Based", "Resident Based", "Territorial Based"], key='-BOR-')],
                   [sg.Submit(), sg.Cancel()]
     ]
     country_window = sg.Window('Adding Countries', editlayout)

     while True:
          event, values = country_window.read()

          if event == sg.WINDOW_CLOSED or event == 'Cancel':
               country_window.close()
               break
          if event == 'Submit':
               country = values['-PLACE-']
               border = values['-BOR-'] 
               adding_countries(country, border)
               country_window.close()
               tax()
          country_window.close()

     
countries = country_list()
def tax():
     sg.theme("DarkBlack1")
     layout = [[sg.Text("Where are you currently living?")],
          [sg.InputOptionMenu(values=countries, key='-COUNT-')],
          [sg.Button('+')],
          [sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Houseing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("What is you total annula salary?(including all side jobs if you have any)")],
          [sg.Text("What is your salary?"), sg.InputText(key='-Salary-', do_not_clear=True)],
          [sg.Text("What are the tax Boundaries for your salary?")],
          [sg.Text("Lower Bound"), sg.InputText(key='-LOW-', do_not_clear=True), sg.Text("Upper bound"), sg.InputText(key='-HIGH-', do_not_clear=True), sg.Text("Percentage of tax"), sg.Spin(values=[i for i in range(100)], initial_value=0, size=(20, 2), enable_events=True, key='-PERCENT-')]
          [sg.Text("How would you and your partner be filing taxes"), sg.Radio("Jointly", "Filling", key='-FILE-'), sg.Radio("Separate", "Filling", key='-SFILE-'), sg.Radio("Head of the House", "Filling", key='-HOH-')],
          [sg.Text("Set the date of when the tax is beeing filed"),sg.Input(key='-PICKUP-', size=(20, 1)), sg.CalendarButton("Filing Date", close_when_date_chosen=True, target='-PICKUP-', location=(0, 0), no_titlebar=False)],
          [sg.Submit(), sg.Button("Back"), sg.Cancel()]
        ]
     
     Window = sg.Window('USA', layout)
     
     while True:
          event, values = Window.read()
          if event == sg.WINDOW_CLOSED or event == 'Cancel':
               Window.close()
               break 
          if event == '+':
               Window.close()
               add_country()
          if event == 'Submit':
               residance = values['-COUNT-']
               salary = values['-Salary-']
               lower_bound = values['-LOW-']
               upper_bound = values['-HIGH-']
               percentage = values['-PERCENT-']
               save_info_to_bracket(residance, lower_bound, upper_bound, percentage)
               save_salary(salary, username, password, residance, lower_bound, upper_bound)
          Window.close()

# for learning purposes
def calculate_tax():
     taxes: List[Tax] = []
     result = 0
     for tax in taxes:
          result += tax.calculate_tax()
     
     print(result)
          
