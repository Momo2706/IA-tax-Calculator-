import PySimpleGUI as sg
from typing import Callable

def go_to(current_window: sg.Window, target: Callable):
    current_window.close()
    target()