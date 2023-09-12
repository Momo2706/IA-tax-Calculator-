import PySimpleGUI as sg  
from ui.login import go_to_login
from ui.router import go_to
from db.country_service import get_phone_codes
from db.database_interface import save_info_to_bracket, save_salary
from db.country_service import get_countries
from globals import session

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
                go_to(person_window, go_to_login)
     person_window.close()

def go_to_tax_info():
     sg.theme("DarkBlack1")
     layout = [[sg.Text("Where are you currently living?")],
          [sg.InputOptionMenu(values=get_countries(), key='-COUNT-')]
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
          if event == 'Submit':
               residance = values['-COUNT-']
               salary = values['-Salary-']
               lower_bound = values['-LOW-']
               upper_bound = values['-HIGH-']
               percentage = values['-PERCENT-']
               save_info_to_bracket(residance, lower_bound, upper_bound, percentage)
               save_salary(salary, session.get_user(), residance, lower_bound, upper_bound)
          Window.close()
