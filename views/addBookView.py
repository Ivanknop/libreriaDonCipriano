import PySimpleGUI as sg
import datetime

def addBookView():
    left_layout = [
        [sg.Text('Título',font='Italic 10',key='title')],
        [sg.InputText('',font='Italic 10',key='newTitle',do_not_clear=False)],
        [sg.Text('Autor',font='Italic 10',key='author')],
        [sg.InputText('',font='Italic 10',key='newAuthor',do_not_clear=False)],
        [sg.Text('Editorial',font='Italic 10',key='editorial')],
        [sg.InputText('',font='Italic 10',key='newEditorial',do_not_clear=False)],
        [sg.Text('Proveedor',font='Italic 10',key='supplier')],
        [sg.InputText(default_text='Propio',font='Italic 10',key='newSupplier')],  
        [sg.Text('Precio de Compra',font='Italic 10',key='purchaseValue')],
        [sg.InputText(default_text=0,font='Italic 10',key='newPurchaseValue')],
        [sg.Text('Porcentaje',font='Italic 10',key='percentage')],
        [sg.InputText(default_text=100,font='Italic 10',key='newPercentage')]
    ]
    right_layout = [
        [sg.Text('Subtítulo',font='Italic 10',key='subTitle')],
        [sg.InputText('',font='Italic 10',key='newSubTitle',do_not_clear=False)],
        [sg.Text('Temática',font='Italic 10',key='category')],
        [sg.InputText('',font='Italic 10',key='newCategory',do_not_clear=False)],
        [sg.Text('Año',font='Italic 10',key='year')],
        [sg.InputText('',font='Italic 10',key='newYear',do_not_clear=False)],
        [sg.Text('Cantidad',font='Italic 10',key='count')],
        [sg.InputText(default_text=1,font='Italic 10',key='newCount')],
        [sg.Text('Pecio de Venta',font='Italic 10',key='saleValue')],
        [sg.InputText(default_text=0,font='Italic 10',key='newSaleValue',enable_events=True)],
        [sg.Text('Notas',font='Italic 10',key='notes')], 
        [sg.InputText(default_text='',font='Italic 10',key='newNotes')],
        [sg.Button('Agregar', font='Italic 8', size=(10, 2), key='addBook')]
        
    ]
    layout = [ [  
        sg.Column(left_layout, element_justification='left',key='leftValues'),
        sg.Column(right_layout,  element_justification='right'),  
    ]]
    return layout