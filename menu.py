import PySimpleGUI as sg 
from ui.personal_info import go_to_personal_info, go_to_tax_info
from db.history_service import get_dates_from_user
from globals import session

#have the graphs and history here
user = session.get_user()
def first_main_menu():
    sg.theme("DarkBlack1")
    menu_window =[[sg.Text("Welcome", key=user)],
                  [sg.Button("New filing"), sg.Button("edit personal info")],
                  [sg.Cancel]
    ]
    window = sg.Window("Main Menu", menu_window)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == "edit personal info":
            go_to_personal_info()
        elif event == "new filing":
            go_to_tax_info()
    window.close()

dates = get_dates_from_user()

def main_menu():
    sg.theme("DarkBlack1")
    menu_window =[[sg.Text("Welcome", key=user)],
                  #make here the graphs for the app
                  [sg.Button("New filing"), sg.Button("edit personal info")],
                  [sg.Cancel]
    ]
    window = sg.Window("Main Menu", menu_window)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == "edit personal info":
            go_to_personal_info()
        elif event == "New filing":
            go_to_tax_info()
    window.close()