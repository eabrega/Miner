from random import randint
from core.math import Point

BOMB_VALUE = -1
gplace = []

def makeGamePlace(width:int, height:int, bombsQuantity:int) -> list[Point]:
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

    bombs = getBombs(place)
    for bomb in bombs:
        neibors = getBombNeibors(bomb, width, height)
        neiborsExcludeBombs = [x for x in neibors if x not in bombs]
        setBombMarkers(neiborsExcludeBombs, place)
    global gplace
    gplace = place
    return place


def getBombs(place:list[Point]) -> list[Point]:
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
    return gplace[point.Y][point.X]

def setValue(point:Point, value)->None:
    gplace[point.Y][point.X] = value
    

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


def setBombMarkers(neibors:list[Point], place:list[Point]) -> None:
    for neibor in neibors:
        if place[neibor.Y][neibor.X] != BOMB_VALUE:
            place[neibor.Y][neibor.X] += 1

def getAllEmptyNeibors(points: list[Point], w, h)-> list[Point]:
    if len(points) == 0:
        return points    

    quantytyNaiborsBefore = len(points)

    for point in points:
        neiborPoints = getEmptyNeibors(point, w, h)      
        for point in neiborPoints:  
            setValue(point, 99)     
            if point not in points:               
                points.append(point)

    if (quantytyNaiborsBefore==len(points)):
        return points           
    return getAllEmptyNeibors(points, w, h)    
    

def getEmptyNeibors(point: Point, w, h):
    emptyNeibors = []
    neibors = getBombNeibors(point, w, h)
    for neibor in neibors:
        if getValue(neibor) == 0:
            emptyNeibors.append(neibor)
    return emptyNeibors

def getNumberNeibors(point: Point, w, h):
    emptyNeibors = []
    neibors = getBombNeibors(point, w, h)
    for neibor in neibors:
        if getValue(neibor) > 0 and getValue(neibor) <9:
            emptyNeibors.append(neibor)
    return emptyNeibors


