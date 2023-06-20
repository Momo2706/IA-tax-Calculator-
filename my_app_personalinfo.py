import PySimpleGUI as sg  
from my_app_functions import USA_single, USA_married, Dutch_single, Dutch_married

def personal_info():
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

     person_window = sg.Window('Tax', layout)

    
     while True:
            event, values = person_window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                person_window.close()
                break   
            elif event == 'Submit':
                if values['-COUNTRY-'][0] == '+1':
                     if values['-MAR-'] == True:
                        person_window.close()
                        USA_married()
                     elif values['-DIV-'] == True or values['-UNMAR-'] == True:
                        person_window.close()
                        USA_single()
                if values['-COUNTRY-'][0] == '+31':
                     if values['-MAR-'] == True:
                        person_window.close()
                        Dutch_married()
                     elif values['-DIV-'] == True or values['-UNMAR-'] == True:
                        person_window.close()
                        Dutch_single()
                if values['-COUNTRY-'][0] == '+34':
                     person_window.close()
                if values['-COUNTRY-'][0] == '+44':
                     person_window.close()
                if values['-COUNTRY-'][0] == '+377':
                     person_window.close()
     person_window.close()
