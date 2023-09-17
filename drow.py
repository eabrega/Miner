from tkinter import *
import tkinter.font as font

def drowBoard(plase):   
    for r in plase:
        drowRow(r)
        print()

def drowRow(cels):
    for c in cels:
        if c != 0:
            print(c, " ", end='')
        else:
            print('_', " ", end='')


root = Tk()
root.title("Сапер")
root.geometry("500x500")
fontObj = font.Font(size=30)

def drowUi(place, w, h):
    for c in range(w):
        root.columnconfigure(index=c, weight=1)
    for r in range(h):
        root.rowconfigure(index=r, weight=1)

    def click(f, sender):
        value = place[f[1]][f[0]]
        match value:
            case 0:
                sender["text"] = " "
            case '*':
                sender["text"] = "*"
            case _:
                sender["text"] = value

    for r in range(w): 
        for c in range(h):
            btn = Button(text="  ",font=fontObj)
            btn.config(command=lambda f=(c,r), b=btn: click(f, b))
            btn.grid(row=r, column=c, sticky=NSEW)
    
    root.mainloop()