import PySimpleGUI as sg 
from ui.personal_info import go_to_personal_info
from my_app_functions import go_to_tax_info
from globals import session

#have the graphs and history here
user = session.get_user()
def main_menu():
    sg.theme("DarkBlack1")
    menu_window =[[sg.Text("Welcome", key=user)],
                  []
    ]
