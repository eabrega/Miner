from ui.drowUi import drowUi
from drowDebug import drowBoard
from game import makeGamePlace

w = 5
h = 5

place = makeGamePlace(w, h, 1)
drowBoard(place)
drowUi(place, False)


#🚩
