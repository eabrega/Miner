from tkinter import Button
from core.math import Point
from drowDebug import mapValue
from ui.helpers.stylesHelpers import getColor

def getBtnValue(value, isDebug:bool) -> str:
    if isDebug:
        return mapValue(value)
    else:
        return "   "
    
def showNeidors(sender: Button):
    sender["state"] = "disabled"
    sender['bg'] = 'gray80'

def showNumbers(sender: Button, value):
    sender['foreground']=getColor(value)
    sender['text'] = value

def getButtonOrdinats(width: int, id: int) -> Point:
    y = id // width 
    x = id - y * width  
    return (Point(x, y))

def getButtonsId(width: int, point:Point)->int:
    return point.Y * width + point.X