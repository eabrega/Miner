from core.math import Point


def drowBoard(plase:list[Point]):   
    for r in plase:
        drowRow(r)
        print()

def drowRow(cels:Point):
    for c in cels:
        if c != 0:
            print(mapValue(c), " ", end='')
        else:
            print('_', " ", end='')

def mapValue(value:int) -> str:
    match value:
        case 0:
            return "  "
        case -1:
            return "*"
        case _:
            return value