import PySimpleGUI as sg
from ui.welcome import go_to_welcome
from model.session import Session

def main():
    go_to_welcome()

if __name__ == "__main__":
      sg.theme("DarkBlack1")
      # logic to init DB
      # Init my_app.db if it doesn't exist.
      main()