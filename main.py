from drowUi import drowUi
from drowDebug import drowBoard
from game import makeGamePlace

w = 10
h = 10

place = makeGamePlace(w, h, 700)
drowBoard(place)
drowUi(place, True)


#🚩
