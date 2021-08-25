import PySimpleGUI as sg
from tema import tema
import interfazCargaLibros

import os 


def interfazInicial():
    
    layout= [
        [sg.Button('Agregar Libro',font='Italic 20',size=(12,3),key='newBook'),
            sg.Button('Editar Libro',font='Italic 20',size=(12,3),key='editLibro'),
            sg.Button('Borrar Libro',font='Italic 20',size=(12,3),key='delLibro')]
    ]
    salir = [[sg.Button('Salir',font='Italic 20',size=(12,3),key='salir')]]
    return layout + salir

def principal():
    alto = 500
    ancho = 900
    tema()    
    ventana = sg.Window ('Librería Don Cipriano',interfazInicial(), size = (ancho,alto),element_justification='center')
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir') :
            break
        if (evento == 'newBook'):
            interfazCargaLibros.inicioConsignas()
        
    ventana.Close()
principal()
