from ui.drowUi import drowUi
from drowDebug import drowBoard
from game import makeGamePlace

w = 10
h = 10

place = makeGamePlace(w, h, 10)
drowBoard(place)
drowUi(place, False)


#🚩
