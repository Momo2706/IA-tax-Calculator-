import PySimpleGUI as sg 
from db.database_interface import country_list, adding_countries


def add_country():
     sg.theme("DarkBlack1")
     editlayout = [[sg.Text("Country"), sg.Input(key='-PLACE-')],
                   [sg.Text("Country_Code"), sg.Input(key='-CODE-')],
                   [sg.Text("Tax Borders")],
                   [sg.Radio("Citizen Based", "BORDER", False, key='-CIT-'), sg.Radio("Resident Based", "BORDER", False, key='-RES-'), sg.Radio("Territorial Based", "BORDER", False, key='-TER-')],
                   [sg.Text("What is the minimun Taxable income on you current place of residance?")],
                   [sg.Input(key='-MIN-')],
                   [sg.Submit(), sg.Cancel()]
     ]
     Country_window = sg.Window('Adding Countries', editlayout)

     while True:
          event, values = Country_window.read()

          if event == sg.WINDOW_CLOSED or event == 'Cancel':
               Country_window.close()
               break
          if event == 'Submit':
               country = values['-PLACE-']
               code = values['-CODE-']
               if values['-CIT-'] == True:
                    border = "Citizen Based"
               elif values['-RES-'] == True:
                    border = "Resident Based"
               elif values['-TER-'] == True:
                    border = "Territorial Based"
               else:
                   sg.popup('Try again')
               taxeble_income = values['-MIN-'] 
               adding_countries(country, code, border, taxeble_income)
               Country_window.close()
               Tax()
          Country_window.close()



countries = country_list()
def Tax():
     sg.theme("DarkBlack1")
     layout = [[sg.Text("Where are you currently living?")],
          [sg.InputOptionMenu(values=countries, key='-COUNT-')],
          [sg.Button('+')],
          [sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Houseing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("What is you total annula salary?(including all side jobs if you have any)")],
          [sg.InputText(key='-Salary-', do_not_clear=True)],
          [sg.Text("How would you and your partner be filing taxes"), sg.Radio("Jointly", "Filling", key='-FILE-'), sg.Radio("Separate", "Filling", key='-SFILE-'), sg.Radio("Head of the House", "Filling", key='-HOH-')],
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
               Residance = values['-COUNT-']
          Window.close()