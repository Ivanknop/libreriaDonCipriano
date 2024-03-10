import PySimpleGUI as sg
import os
import datetime
image_dir = os.path.dirname(__file__)
def searchView():
    layout = [
                [sg.Text('Título'), sg.InputText(key='-TITLE-')],
                [sg.Text('Autor'), sg.InputText(key='-AUTHOR-')],
                [sg.Text('Categoría'), sg.InputText(key='-CATEGORY-')],
                [sg.Button('Buscar',key='search_book')]
    ]
    return layout
