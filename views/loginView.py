import PySimpleGUI as sg
from app import *

def value_login(anUser,aPass,aLogin):

    if (anUser == 'Nico') and (aPass == '22'):
        sg.popup('Login OK')
        return True
    else:
        sg.popup('Error de usuario y/o contraseña')
        return False

def login():
    login = False
    layout=[ 
        [sg.Text('Ingrese Usuario',font='Italic 10',key='user',size=(20,1))],
        [sg.InputText('',font='Italic 10',key='user_key',do_not_clear=False,size=(10,2))],
        [sg.Text('Ingrese Password',font='Italic 10',key='pass',size=(20,1))],
        [sg.InputText('',font='Italic 10',key='pass_key',do_not_clear=False,size=(10,2))],
        [sg.Button('Ingresar',key='login')]
           ]
    window_main = sg.Window('Librería Don Cipriano', layout, element_justification='center', resizable=True)
    window_main.finalize()
    
    while login==False:
        event, values = window_main.read()
        if event == sg.WINDOW_CLOSED or event == 'exit':
            break
        elif event == 'login':
            login = value_login(values['user_key'],values['pass_key'],login)
            if login:
                break
        elif login:
            break
    window_main.close()

