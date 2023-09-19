from tkinter import *
from drowDebug import mapValue
from ui.helpers.styles import getColor
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
        value = place[f.Y][f.X]
        # sender["text"]=mapValue(value)
        id = buttons.index(sender)
        ord = getButtonOrdinats(w, id)
        neibors = getAllEmptyNeibors(ord, w, h)
        for neibor in neibors:
            id = getButtonsId(w, neibor)
            showNeidors(buttons[id])
        
    for row in range(h): 
        for cell in range(w):
            btn = Button(text=getBtnValue(place[row][cell], isDebug),font=fontObj, foreground=getColor(place[row][cell]))
            btn.config(command=lambda f=Point(cell,row), b=btn: click(f, b))
            btn.grid(row=row, column=cell, sticky=NSEW)   
            buttons.append(btn)        
    
    root.mainloop()

def getBtnValue(value, isDebug:bool) -> str:
    if isDebug:
        return mapValue(value)
    else:
        return "   "
    
def showNeidors(sender: Button):
    sender["state"] = "disabled"
    sender["bg"] = 'gray'

def getButtonOrdinats(width: int, id: int) -> Point:
    y = id // width 
    x = id - y * width  
    return (Point(x, y))

def getButtonsId(width: int, point:Point)->int:
    return point.Y * width + point.X