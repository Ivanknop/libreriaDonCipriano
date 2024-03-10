import PySimpleGUI as sg
import os

image_dir = os.path.dirname(__file__)
def catalogheView(books):
    if books:
      data = [[book.id, book.title, book.author, book.category, book.supplier] for book in books]
      headers = data[0]
      tabla = sg.Table(
                values=data[0:], 
                headings=headers,
                auto_size_columns=False,
                display_row_numbers=False,
                col_widths=15,
                justification='left'
              ) 
      layout_catalog = [
            [sg.Text('Catálogo de Libros')],
           [tabla]
        ]
    else:
      layout_catalog = [
            [sg.Text('No hay libros en el catálogo.')]]
    
    return layout_catalog
