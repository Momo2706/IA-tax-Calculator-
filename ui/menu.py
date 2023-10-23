import PySimpleGUI as sg 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ui.personal_info import go_to_personal_info, go_to_tax_info
from db.history_service import get_history_by_user
from ui.router import go_to
from globals import session
    
def first_main_menu():
    sg.theme("DarkBlack1")
    user = session.get_user()
    menu_window =[[sg.Text("Welcome", key=user)],
                  [sg.Button("New filing"), sg.Button("edit personal info")],
                  [sg.Cancel()]
    ]

    window = sg.Window("Main Menu", menu_window)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == "New filing":
            go_to(window, go_to_tax_info)
        elif event == "edit personal info":
            go_to(window, go_to_personal_info)
    window.close()

def history_graph(filling_dates, tax_amount):
     # Set the figure size (width, height) in inches
    plt.figure(figsize=(5, 3))
    plt.plot(filling_dates, tax_amount, color='blue', marker='o')
    plt.title('Taxing history', fontsize=8)
    plt.xlabel('dates', fontsize=4)
    plt.ylabel('Tax paid', fontsize=4)
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=4)
    plt.grid(True)
    return plt.gcf()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def main_menu():
    sg.theme("DarkBlack1")
    user = session.get_user()
    menu_window =[[sg.Text(f"Welcome, {user.username}")],
                  [sg.Canvas(size=(1200,600), key='-CANVAS-')],
                  [sg.Button("New filing"), sg.Button("edit personal info")],
                  [sg.Cancel()]
    ]
    window = sg.Window("Main Menu", menu_window, finalize=True, element_justification='center')
    histories = get_history_by_user(user)
    dates = []
    amount = []
    for history in histories:
        dates.append(history.date)
        amount.append(history.tax_amount)

    figure = history_graph(dates, amount)

    draw_figure(window['-CANVAS-'].TKCanvas, figure)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        elif event == "edit personal info":
            go_to(window, go_to_personal_info)
        elif event == "New filing":
            go_to(window, go_to_tax_info)
    window.close()