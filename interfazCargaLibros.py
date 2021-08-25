import PySimpleGUI as sg
from tema import *


def interfazPrincipal ():
    layout = [
        [sg.Text('Título',font='Italic 10',key='titulo')],
        [sg.InputText('',font='MedievalSharp 10',key='newTitle',do_not_clear=False)],
        [sg.Text('Subtítulo',font='Italic 10',key='subtitulo')],
        [sg.InputText('',font='MedievalSharp 10',key='newSubtitle',do_not_clear=False)],
        [sg.Text('Autor',font='Italic 10',key='autor')],
        [sg.InputText('',font='MedievalSharp 10',key='newAuthor',do_not_clear=False)],
        [sg.Text('Editorial',font='Italic 10',key='editorial')],
        [sg.InputText('',font='MedievalSharp 10',key='newEditorial',do_not_clear=False)],
        [sg.Text('Proveedor',font='Italic 10',key='proveedor')],
        [sg.InputText('',font='MedievalSharp 10',key='newProv',do_not_clear=False)],
        [sg.Text('Temática',font='Italic 10',key='tematica')],
        [sg.InputText('',font='MedievalSharp 10',key='newThem',do_not_clear=False)],
        [sg.Text('Observaciones',font='Italic 10',key='observaciones')],
        [sg.InputText('',font='MedievalSharp 10',key='newObs',do_not_clear=False)],
        [sg.Text('Precio',font='Italic 10',key='precio')],
        [sg.InputText('',font='MedievalSharp 10',key='newCost',do_not_clear=False)]
    ]
    layoutBotones = [
        [sg.Button('Agregar Libro',font='Italic 10',size=(10,2),border_width=1,key = 'newBook'),
        sg.Button('Salir',font='Italic 10',size=(10,2),border_width=1,key = 'salir')
        ]
    ]
    colPreguntas= layout
    colBotones = layoutBotones

    layout3 = [
            
            [sg.Column(colPreguntas,justification='center',key='colPreg'),
            sg.Column(colBotones,justification='center',key='colBot')]
    ]
    return layout3  
    
def inicioConsignas():
    altura = 500
    largo = 450
    tema()
    ventana = sg.Window ('Juego Cervantes',interfazPrincipal(), size = (largo,altura))
    ventana.Finalize()

    while True:
        evento, value = ventana.read()
        if (evento == None or evento == 'salir') :
            break
    ventana.Close()
