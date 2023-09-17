from random import randint


def makeGamePlace(width, height, bombs):
    plase = [[0 for x in range(width)] for y in range(height)]

    if width * height * 0.15 < bombs:
        bombs = width * height * 0.15

    bombsCount = 0
    while bombsCount < bombs:
        randomX = randint(0, width-1)
        randomY = randint(0, height-1)
        if plase[randomY][randomX] != '*':
            plase[randomY][randomX] = '*'
            bombsCount = bombsCount+1

    bombs = getBombs(plase)
    for bomb in bombs:
        neibors = getBombNeibors(bomb, width, height)
        neiborsExcludeBombs = [x for x in neibors if x not in bombs]
        bombMarkers(neiborsExcludeBombs, plase)
    return plase


def getBombs(place):
    mines = []
    x = 0
    y = 0
    for row in place:
        x = 0
        for c in row:
            if c == '*':
                mines.append((x, y))
            x = x+1
        y = y+1
    return mines


def getBombNeibors(bomb, width, height):
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


def filtredNeibors(neibor, width, height):
    if (neibor[0] >= 0 and neibor[0] <= width-1 and neibor[1] >= 0 and neibor[1] <= height-1):
        return True
    return False


def bombMarkers(neibors, place):
    for neibor in neibors:
        place[neibor[1]][neibor[0]] += 1
