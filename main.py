from drowUi import drowUi
from drowDebug import drowBoard
from game import makeGamePlace

w = 5
h = 5

place = makeGamePlace(w, h, 700)
drowBoard(place)
drowUi(place, True)


#🚩
