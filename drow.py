
def drowBoard(plase):   
    for r in plase:
        drowRow(r)
        print()

def drowRow(cels):
    for c in cels:
        if c != 0:
            print(c, " ", end='')
        else:
            print('_', " ", end='')