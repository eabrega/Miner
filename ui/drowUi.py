from tkinter import *
from ui.helpers.uiHelpers import *
from tkinter import font
from core.math import Point
from game import *

root = Tk()
root.title("Сапер")
root.geometry("500x500")
fontObj = font.Font(size=30, weight='bold')


def drowUi(place:list[Point], isDebug:bool)->None:
    w = len(place[0])
    h = len(place)
    for cell in range(h):
        root.columnconfigure(index=cell, weight=1)
    for row in range(w):
        root.rowconfigure(index=row, weight=1)

    buttons=[]

    def click(f:Point, sender):
        id = buttons.index(sender)
        point = getButtonOrdinats(w, id)
        showNumbers(sender, getBtnValue(place[point.Y][point.X], True))
        points = getEmptyNeibors(point, w, h)
        neibors = getAllEmptyNeibors(points, w, h)
        for neibor in neibors:          
            id = getButtonsId(w, neibor)
            showNeidors(buttons[id])
            nn = getNumberNeibors(neibor, w ,h)
            for n in nn: 
                id = getButtonsId(w, n)
                showNumbers(buttons[id], place[n.Y][n.X])
        
    for row in range(h): 
        for cell in range(w):
            btn = Button(text=getBtnValue(place[row][cell], isDebug), font=fontObj)
            btn.config(command=lambda f=Point(cell,row), b=btn: click(f, b))
            btn.grid(row=row, column=cell, sticky=NSEW)   
            buttons.append(btn)        
    
    root.mainloop()
