import PySimpleGUI as sg
import re
from theme import theme
from views.addBookView import * 
from views.catalogheView import *
from views.maintenanceView import *
from views.sellsView import *
from views.sellBooksView import *
from views.stadisticsView import *
from views.searchView import *
from views.welcomeView import *
from book import Book



def validate_input(text):
    pattern = r'^[0-9]*$'
    print (text.isdigit())
    if re.match(pattern, text) is None:
        return False
    return True

def validate_values(values):
    return validate_input(values['newSaleValue'])

def addBook(aBook,values):
    if validate_values(values):
        book_values={'title':values['newTitle'],
                 'author':values['newAuthor'],
                 'subTitle':values['newSubTitle'],
                 'photo':values['newTitle'],
                 'percentage':values['newPercentage'],
                 'notes':values['newNotes'],
                 'purchaseDate':values['newPurchaseDate'],
                 'saleDate':values['newSaleDate'],
                 'count':values['newCount'],
                 'editorial':values['newEditorial'],
                 'supplier':values['newSupplier'],
                 'category':values['newCategory'],
                 'purchaseValue':values['newPurchaseValue'],
                 'saleValue':values['newSaleValue'],
                 'year':values['newYear']}
        book = Book(book_values)
        print (book)
    else:
        sg.popup_error('Por favor, ingrese solo números.')

def updateCenterView(window,event,activeView):
    window[activeView].update(visible=False)
    window[f'CENTER-{event}'].update(visible=True)

def initialView():
     
    left_layout = [
    [sg.Text("Opciones", font='Italic 20')],
    [sg.Button('Agregar Libro', font='Italic 10', size=(12, 2), key='addBookView')],
    [sg.Button('Búsqueda', font='Italic 10', size=(12, 2), key='searchView')],
    [sg.Button('Catálogo', font='Italic 10', size=(12, 2), key='catalogheView')],
    [sg.Button('Mantenimiento', font='Italic 10', size=(12, 2), key='maintenanceView')],
    [sg.Button('Facturar', font='Italic 10', size=(12, 2), key='sellBooksView')],
    [sg.Button('Caja', font='Italic 10', size=(12, 2), key='sellsView')],
    [sg.Button('Estadísticas', font='Italic 10', size=(12, 2), key='stadisticsView')],
    [sg.Button('volver',font='Italic 10',size=(12,2),key='return')],
    [sg.Button('salir',font='Italic 10',size=(12,2),key='exit')]
    ]

# Definir el diseño de la ventana principal
    layout = [
    [
        sg.Column(left_layout, element_justification='left',expand_y=True,expand_x=True),
        sg.Column(welcomeView(), size=(800, 500), background_color='#222E50', key='CENTER-welcomeView',element_justification='center',expand_y=True,expand_x=True,visible=True),
        sg.Column(addBookView(), size=(800, 500), background_color='#222E50', key='CENTER-addBookView',expand_y=True,expand_x=True,visible=False),
        sg.Column(searchView(), size=(800, 500), background_color='#222E50', key='CENTER-searchView',expand_y=True,expand_x=True,visible=False) ,
        sg.Column(catalogheView(), size=(800, 500), background_color='#222E50', key='CENTER-catalogheView',expand_y=True,expand_x=True,visible=False),
        sg.Column(maintenanceView(), size=(800, 500), background_color='#222E50', key='CENTER-maintenanceView',expand_y=True,expand_x=True,visible=False) ,
        sg.Column(sellBooksView(), size=(800, 500), background_color='#222E50', key='CENTER-sellBooksView',expand_y=True,expand_x=True,visible=False) ,
        sg.Column(sellsView(), size=(800, 500), background_color='#222E50', key='CENTER-sellsView',expand_y=True,expand_x=True,visible=False),
        sg.Column(stadisticsView(), size=(800, 500), background_color='#222E50', key='CENTER-stadisticsView',expand_y=True,expand_x=True,visible=False) 
    ]
]
    return layout

def main():
    theme() 
    window = sg.Window ('Librería Don Cipriano',initialView(), element_justification='center',resizable=True)
    window.Finalize()
    
    activeView = 'CENTER-welcomeView'
    no_view_events = ['newSaleValue','addBook','return']
    while True:
        event, values = window.read()
        if (event == None or event == 'exit') :
            break
        if event == 'return':
            window[activeView].update(visible=False)
            window[f'CENTER-welcomeView'].update(visible=True)
        if event == 'addBook':
            addBook(window,values)
        if event in no_view_events:
            continue
        else :            
            window[f'CENTER-welcomeView'].update(visible=False)
            updateCenterView (window, event, activeView)  
            activeView = f'CENTER-{event}'      
    window.Close()
main()