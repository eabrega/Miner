from ui.drowUi import drowUi
from drowDebug import drowBoard
from game import makeGame

width = 10
height = 10
bombs = 15

gameBoard = makeGame(width, height, bombs)
drowBoard(gameBoard)
drowUi(gameBoard, False)

#🚩
