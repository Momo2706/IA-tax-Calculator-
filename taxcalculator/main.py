import PySimpleGUI as sg
from taxcalculator.ui.welcome import go_to_welcome
from taxcalculator.db.database_interface import is_db_connected
from taxcalculator.db.create_db import creat_db

def main():
    go_to_welcome()
 
if __name__ == "__main__":
      sg.theme("DarkBlack1")
      if is_db_connected() == False:
           creat_db()
           main() 
      else:
           main()