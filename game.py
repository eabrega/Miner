from random import randint

def makeGamePlace(width:int, height:int, bombs:int) -> list[list[int]]:
    place = [[0 for x in range(width)] for y in range(height)]

    if width * height < bombs:
        bombs = width * height * 0.15

    bombsCount = 0
    while bombsCount < bombs:
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
    return place


def getBombs(place:list[list[int]]) -> list[list(int,int)]:
    bombsPositions = []
    x = 0
    y = 0
    for row in place:
        x = 0
        for c in row:
            if c == -1:
                bombsPositions.append((x, y))
            x = x+1
        y = y+1
    return bombsPositions


def getBombNeibors(bomb:list[(int, int)], width, height):
    neibors = []
    neibors.append((bomb[0]-1, bomb[1]-1))  # 1
    neibors.append((bomb[0], bomb[1]-1))  # 2
    neibors.append((bomb[0]+1, bomb[1]-1))  # 3

    neibors.append((bomb[0]-1, bomb[1]))  # 4
    neibors.append((bomb[0]+1, bomb[1]))  # 5

    neibors.append((bomb[0]-1, bomb[1]+1))  # 6
    neibors.append((bomb[0], bomb[1]+1))  # 7
    neibors.append((bomb[0]+1, bomb[1]+1))  # 8
    return list(filter(lambda x: filtredNeibors(x, width, height), neibors))


def filtredNeibors(neibor:list[(int, int)], width, height):
    if (neibor[0] >= 0 and neibor[0] <= width-1 and neibor[1] >= 0 and neibor[1] <= height-1):
        return True
    return False


def setBombMarkers(neibors, place:list[list[int]]):
    for neibor in neibors:
        place[neibor[1]][neibor[0]] += 1
