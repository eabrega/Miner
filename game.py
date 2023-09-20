from random import randint
from core.math import Point

BOMB_VALUE = -1
SWOWED_EMPTY_CELL_VALUE = 99
globalGameBoard = []

def makeGame(width:int, height:int, bombsQuantity:int) -> list[Point]:
    place = [[0 for x in range(width)] for y in range(height)]

    if width * height < bombsQuantity:
        bombsQuantity = width * height * 0.15

    bombsCount = 0
    while bombsCount < bombsQuantity:
        randomX = randint(0, width-1)
        randomY = randint(0, height-1)
        if place[randomY][randomX] != -1:
            place[randomY][randomX] = -1
            bombsCount = bombsCount+1

    global globalGameBoard
    globalGameBoard = place
    bombs = getBombPositions(place)
    for bomb in bombs:
        neibors = getBombNeibors(bomb, width, height)
        neiborsExcludeBombs = [x for x in neibors if x not in bombs]
        setBombMarkers(neiborsExcludeBombs)  
    return place

def getBombPositions(place:list[Point]) -> list[Point]:
    bombsPositions = []
    x = 0
    y = 0
    for row in place:
        x = 0
        for c in row:
            if c == BOMB_VALUE:
                bombsPositions.append(Point(x, y))
            x = x+1
        y = y+1
    return bombsPositions

def getValue(point:Point)->int:
    return globalGameBoard[point.Y][point.X]

def setValue(point:Point, value)->None:
    globalGameBoard[point.Y][point.X] = value
    
def getBombNeibors(bomb:Point, width, height) -> list[Point]:
    neibors = []

    neibors.append(Point(bomb.X-1, bomb.Y-1))  # 1
    neibors.append(Point(bomb.X, bomb.Y-1))  # 2
    neibors.append(Point(bomb.X+1, bomb.Y-1))  # 3

    neibors.append(Point(bomb.X-1, bomb.Y))  # 4
    neibors.append(Point(bomb.X+1, bomb.Y))  # 5

    neibors.append(Point(bomb.X-1, bomb.Y+1))  # 6
    neibors.append(Point(bomb.X, bomb.Y+1))  # 7
    neibors.append(Point(bomb.X+1, bomb.Y+1))  # 8
    return list(filter(lambda x: filtredNeibors(x, width, height), neibors))

def filtredNeibors(neibor:Point, width, height)-> bool:
    if (neibor.X >= 0 and neibor.X <= width-1 and neibor.Y >= 0 and neibor.Y <= height-1):
        return True
    return False

def setBombMarkers(neibors:list[Point]) -> None:
    for neibor in neibors:
        value = getValue(neibor)
        if value != BOMB_VALUE:
            value += 1
            setValue(neibor, value)

def getAllEmptyNeibors(points: list[Point], w, h)-> list[Point]:
    quantytyNaiborsBefore = len(points)
    if quantytyNaiborsBefore == 0:
        return points    

    for point in points:
        neiborPoints = getNeiborsByRules(point, lambda x: x==0, w, h)      
        for point in neiborPoints:  
            setValue(point, SWOWED_EMPTY_CELL_VALUE)     
            if point not in points:               
                points.append(point)

    if (quantytyNaiborsBefore==len(points)):
        return points           
    return getAllEmptyNeibors(points, w, h)    
    
def getNeiborsByRules(point: Point, rules, w, h):
    emptyNeibors = []
    neibors = getBombNeibors(point, w, h)
    for neibor in neibors:
        if rules(getValue(neibor)):
            emptyNeibors.append(neibor)
    return emptyNeibors
