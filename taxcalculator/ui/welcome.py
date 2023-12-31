import PySimpleGUI as sg
from taxcalculator.ui.logo import IMAGE
from taxcalculator.ui.router import go_to
from taxcalculator.ui.login import go_to_login
from taxcalculator.ui.signup import go_to_signup

LOGIN_BUTTON_EVENT = 'Login'
SIGNUP_BUTTON_EVENT = 'Signup'
OUR_STORY_BUTTON_EVENT = 'Our Story'
CANCEL_BUTTON_EVENT = 'Cancel'

sg.theme("DarkBlack1")

WELCOME_WINDOW = [[sg.Image(source = IMAGE, key=('-IMAGE-'), expand_x=True, expand_y=True, size=(300,300))],
          [sg.Text("Hello and welcome to EASY-TAX, an app dedicated to helping people file their income tax.")],
          [sg.Text("Our app will help you file taxes for any of the countries that appear in the lists.")],
          [sg.Text("We hope you join us in helping you have a better financial status.")],
          [sg.Button(LOGIN_BUTTON_EVENT), sg.Button(SIGNUP_BUTTON_EVENT), sg.Cancel(), sg.Button(OUR_STORY_BUTTON_EVENT)]
]

def go_to_welcome():
    sg.theme("DarkBlack1")
    window = sg.Window('Welcome', WELCOME_WINDOW)
    while True:
            event, _ = window.read()

            if event == sg.WINDOW_CLOSED or event == CANCEL_BUTTON_EVENT:
                break

            if event == LOGIN_BUTTON_EVENT:
                #send user to the log in window 
                go_to(window, go_to_login)

            if event == SIGNUP_BUTTON_EVENT:
                #sends user ti the sign up window 
                go_to(window, go_to_signup)
                
            if event ==  OUR_STORY_BUTTON_EVENT:
                #a brief story of the supposed company
                sg.popup('A few years ago my brother graduated High school and moved to the Netherlabds to study. There he faced a few problems mainly the dutch housing crisis among others.' , 'A few years back he had finally found a house to stay in but the problem is that he had no idea on how taxes are filed so fo the most part my father was the one who did them for him.' , 'But my brother wasnt fund of the idea as he had moved away to have more liberty of his parents.' , 'So he had spoken to me to see if i had amy idea on how he could fix this whole ordeal, i thought for a while but all the ideas i could think of werent proper for a collage student.', 'Then i had gotten it an app that could atleast help hiom know how much he has to pay in taxes and so with some discussions with my computer science advisor he had helped me make the idea into a reality and so I came up with "EASY-TAX"', title="Our Story")
    window.close() 