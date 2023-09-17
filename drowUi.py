from tkinter import *
from drowDebug import mapValue
from tkinter import font

root = Tk()
root.title("Сапер")
root.geometry("500x500")
fontObj = font.Font(size=30, weight='bold')

def drowUi(place:list[list], isDebug:bool)->None:
    w = len(place[0])
    h = len(place)
    for cell in range(h):
        root.columnconfigure(index=cell, weight=1)
    for row in range(w):
        root.rowconfigure(index=row, weight=1)

    def click(f:list[int], sender):
        value = place[f[1]][f[0]]
        sender["text"]=mapValue(value)

    for row in range(h): 
        for cell in range(w):
            btn = Button(text=getBtnValue(place[row][cell], isDebug),font=fontObj, foreground=getColor(place[row][cell]))
            btn.config(command=lambda f=(cell,row), b=btn: click(f, b))
            btn.grid(row=row, column=cell, sticky=NSEW)
    
    root.mainloop()

def getBtnValue(value, isDebug:bool) -> str:
    if isDebug:
        return mapValue(value)
    else:
        return "   "

def getColor(value: int)->str:
    match value:
        case 1:
            return 'blue'
        case 2:
            return 'green'
        case 3:
            return 'red'
        case 4:
            return 'blue4'
        case -1:
            return 'black'
        case _:
            return 'red4'