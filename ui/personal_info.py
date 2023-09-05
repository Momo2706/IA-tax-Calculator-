import PySimpleGUI as sg  
from ui.login import go_to_login
from ui.router import go_to

sg.theme("DarkBlack1")

layout = [[sg.Text("Name:"), sg.InputText(key='-NAME-', do_not_clear=True, size=(35,1))],
          [sg.Text("Lastname(s): "), sg.InputText(key='-LASTNAME-', do_not_clear=True, size=(29,1))],
          [sg.Text("Email:"), sg.InputText(key='-EMAIL-', do_not_clear=True, size=(35,1))],
          [sg.Text("Phone Number: "), sg.Listbox(values=['+1', '+31', '+34', '+44', '+377'], select_mode="single", key='-COUNTRY-'), sg.InputText(key='-PHONE-', do_not_clear=True, size=(19,1))],
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
            event, values = person_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break   
            elif event == 'Submit':
                go_to(person_window, go_to_login)
     person_window.close()