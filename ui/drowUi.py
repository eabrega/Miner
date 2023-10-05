from tkinter import Tk, NSEW
from ui.helpers.uiHelpers import *
from tkinter import font
from core.math import Point
from game import *

root = Tk()
root.title("Сапер")
root.geometry("500x500")
fontObj = font.Font(size=30, weight='bold')


def drowUi(place:list[list[int]], isDebug:bool)->None:
    w = len(place[0])
    h = len(place)
    for cell in range(h):
        root.columnconfigure(index=cell, weight=1)
    for row in range(w):
        root.rowconfigure(index=row, weight=1)

    buttons=[]

    def click(sender):
        id = buttons.index(sender)
        point = getButtonOrdinats(w, id)
        showNumbers(sender, getBtnValue(place[point.Y][point.X], True))
        points = getNeiborsByRules(point, lambda x: x==0, w, h)
        neibors = getAllEmptyNeibors(points, w, h)
        for neibor in neibors:          
            id = getButtonsId(w, neibor)
            showNeidors(buttons[id])
            numberedNeibors = getNeiborsByRules(neibor, lambda x: x>0 and x<9, w ,h)
            for neibor in numberedNeibors: 
                id = getButtonsId(w, neibor)
                showNumbers(buttons[id], place[neibor.Y][neibor.X])
        
    for row in range(h): 
        for cell in range(w):
            btn = Button(text=getBtnValue(place[row][cell], isDebug), font=fontObj)
            btn.config(command=lambda b=btn: click(b))
            btn.grid(row=row, column=cell, sticky=NSEW)   
            buttons.append(btn)        
    
    root.mainloop()
