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
    if validate_input(values['newSaleValue']) == False:
        return False, 'Valor de Venta'
    elif validate_input(values['newPercentage']) == False:
        return False, 'Porcentaje'
    elif validate_input(values['newCount']) == False:
        return False, 'Cantidad'
    elif validate_input(values['newPurchaseValue']) == False:
        return False, 'Valor de Compra'
    elif validate_input(values['newYear']) == False:
        return False, 'Año'
    else:
        return True,'' 
   
def addBook(windows,values):
    purchase_date = datetime.date.today()
    rev_date=datetime.date(1917,11,7)
    valid_values,tag =validate_values(values)
    if valid_values:
        book_values={'title':values['newTitle'],
                 'author':values['newAuthor'],
                 'subTitle':values['newSubTitle'],
                 'photo':values['newTitle'],
                 'percentage':values['newPercentage'],
                 'notes':values['newNotes'],
                 'purchaseDate':purchase_date,
                 'saleDate':rev_date,
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
        sg.popup_error(f'El dato {tag} debe ser un número.')

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
        sg.Column(left_layout, element_justification='left',vertical_scroll_only=True),
        sg.Column(welcomeView(), size=(800, 500), background_color='#222E50', key='CENTER-welcomeView',element_justification='center',vertical_scroll_only=True,visible=True),
        sg.Column(addBookView(), size=(800, 500), background_color='#222E50', key='CENTER-addBookView',vertical_scroll_only=True,visible=False),
        sg.Column(searchView(), size=(800, 500), background_color='#222E50', key='CENTER-searchView',vertical_scroll_only=True,visible=False) ,
        sg.Column(catalogheView(), size=(800, 500), background_color='#222E50', key='CENTER-catalogheView',vertical_scroll_only=True,visible=False),
        sg.Column(maintenanceView(), size=(800, 500), background_color='#222E50', key='CENTER-maintenanceView',vertical_scroll_only=True,visible=False) ,
        sg.Column(sellBooksView(), size=(800, 500), background_color='#222E50', key='CENTER-sellBooksView',vertical_scroll_only=True,visible=False) ,
        sg.Column(sellsView(), size=(800, 500), background_color='#222E50', key='CENTER-sellsView',vertical_scroll_only=True,visible=False),
        sg.Column(stadisticsView(), size=(800, 500), background_color='#222E50', key='CENTER-stadisticsView',vertical_scroll_only=True  ,visible=False) 
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
        elif event == 'return':
            window[activeView].update(visible=False)
            window[f'CENTER-welcomeView'].update(visible=True)
        elif event == 'addBook':
            addBook(window,values)
        elif event in no_view_events:
            continue
      
        else :            
            window[f'CENTER-welcomeView'].update(visible=False)
            updateCenterView (window, event, activeView)  
            activeView = f'CENTER-{event}'      
    window.Close()
main()