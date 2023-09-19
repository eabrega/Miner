def getColor(value: int)->str:
    match value:
        case 1:
            return 'blue'
        case 2:
            return 'green'
        case 3:
            return 'red'
        case 4:
            return 'blue4'
        case -1:
            return 'black'
        case _:
            return 'red4'