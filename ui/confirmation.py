import PySimpleGUI as sg 
from ui.router import go_to


def confirm_personal_info_changes_successful():
    from ui.menu import main_menu
    sg.theme("DarkBlack1")
    menu_window =[[sg.Text("The changes to you personal info were succesful")],
                  [sg.Button("Main Menu"), sg.Button('Leave')],
    ]
    window = sg.Window("Main Menu", menu_window)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Leave':
            break
        if event == "Main Menu":
            go_to(window, main_menu)
    window.close()


#put how much they have to pay in taxes
def confirm_tax_filling():
    from ui.menu import main_menu
    sg.theme("DarkBlack1")
    menu_window =[[sg.Text("your taxes")],
                  [sg.Button("Main Menu"), sg.Button('Leave')],
    ]
    window = sg.Window("Main Menu", menu_window)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Leave':
            break
        if event == "Main Menu":
            go_to(window, main_menu)
    window.close()