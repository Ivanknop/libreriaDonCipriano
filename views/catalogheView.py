import PySimpleGUI as sg
import os

image_dir = os.path.dirname(__file__)
def catalogheView():
    layout = [
        [sg.Text("Vista para VER CATÁLOGO libro",font='Italic 30',justification='center',pad=((200,200),(0,0)))],
          [sg.Image(filename=os.path.join(image_dir,'..','images','in_building.png'),pad=((250,250),(100,100)))]
    ]
    return layout