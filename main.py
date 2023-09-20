from ui.drowUi import drowUi
from drowDebug import drowBoard
from game import makeGamePlace

w = 15
h = 15

place = makeGamePlace(w, h, 30)
drowBoard(place)
drowUi(place, False)


#🚩
