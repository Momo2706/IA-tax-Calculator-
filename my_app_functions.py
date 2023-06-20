import PySimpleGUI as sg 

def USA_single():
     sg.theme("DarkBlack1")
     a_layout = [[sg.Text("Which state do you live in?")],
          [sg.InputOptionMenu(values=['California', 'New York', 'Colorado', 'Virginia'], key='-STATES-')],
          [sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Houseing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("What is you total annula salary?(including all side jobs if you have any)")],
          [sg.InputText(key='-Salary-', do_not_clear=True)],
          [sg.Text("Deductions if any?")],
          [sg.Button("+")],
          [sg.Submit(), sg.Button("Back"), sg.Cancel()]
        ]

     AMERICAN_Window = sg.Window('USA', a_layout)

    
     while True:
            event, values = AMERICAN_Window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                AMERICAN_Window.close()
                break  
            if event == 'Submit':
                State = values['-STATES-']
                if State == "New York":
                     break
                if State == "California":
                     break
                if State == "Colorado":
                     break
                if State == "Virgina":
                     break
     AMERICAN_Window.close()

def USA_married():
    sg.theme("DarkBlack1")
    usalayout = [[sg.Text("Which state do you live in?")],
          [sg.InputOptionMenu(values=['California', 'New York', 'Colorado', 'Virginia'], key='-STATES-')],
          [sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Houseing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("What is you total annula salary?(including all side jobs if you have any)")],
          [sg.InputText(key='-Salary-', do_not_clear=True)],
          [sg.Text("How would you and your partner be filing taxes"), sg.Radio("Jointly", "Filling", key='-FILE-'), sg.Radio("Separate", "Filling", key='-SFILE-'), sg.Radio("Head of the House", "Filling", key='-HOH-')],
          [sg.Text("Deductions if any?")],
          [sg.Button("+")],
          [sg.Submit(), sg.Button("Back"), sg.Cancel()]
        ]

    AMERICAN_Window = sg.Window('USA', usalayout)

    
    while True:
            event, values = AMERICAN_Window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                AMERICAN_Window.close()
                break 
            if event == 'Submit':
                State = values['-STATES-']
                if State == "New York":
                     break
                if State == "California":
                     break
                if State == "Colorado":
                     break
                if State == "Virgina":
                     break
    AMERICAN_Window.close()

def Dutch_single():
     sg.theme("DarkBlack1")
     n_layout = [[sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Houseing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("What is you total annula salary?(including all side jobs if you have any)")],
          [sg.InputText(key='-Salary-', do_not_clear=True)],
          [sg.Text("Deductions if any?")],
          [sg.Button("+")],
          [sg.Submit(), sg.Button("Back"), sg.Cancel()]
        ]

     DUTCH_Window = sg.Window('USA', n_layout)

    
     while True:
            event, values = DUTCH_Window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                DUTCH_Window.close()
                break  
     DUTCH_Window.close()

def Dutch_married():
    sg.theme("DarkBlack1")
    ne_layout = [[sg.Text("Do you live in a house or apartment.")],
          [sg.Radio("House", "Houseing", key='-HOUSE-'), sg.Radio("Appartment", "Housing", key='-APPA-')],
          [sg.Text("What is you total annula salary?(including all side jobs if you have any)")],
          [sg.InputText(key='-Salary-', do_not_clear=True)],
          [sg.Text("How would you and your partner be filing taxes"), sg.Radio("Jointly", "Filling", key='-FILE-'), sg.Radio("Separate", "Filling", key='-SFILE-'), sg.Radio("Head of the House", "Filling", key='-HOH-')],
          [sg.Text("Deductions if any?")],
          [sg.Button("+")],
          [sg.Submit(), sg.Button("Back"), sg.Cancel()]
        ]
    DUTCH_Window = sg.Window('USA', ne_layout)

    while True:
            event, values = DUTCH_Window.read()

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                DUTCH_Window.close()
                break 
            DUTCH_Window.close()