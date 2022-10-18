signos = (
    [0, 'Macaco'], [1, 'Cão'], [2, 'Galo'], [3, 'Porco'], [4, 'Rato'], [5, 'Boi'],
    [6, 'Tigre'], [7, 'Coelho'], [8, 'Dragão'], [9, 'Serpente'], [10, 'Cavalo'], [11, 'Carneiro']
    )

def decSigno():
    nasc = int(input("Digite o ano que você nasceu: "))

    if nasc % 12 == 0:
        print(signos[0][1])
    elif nasc % 12 == 1:
        print(signos[1][1])
    elif nasc % 12 == 2:
        print(signos[2][1])
    elif nasc % 12 == 3:
        print(signos[3][1])
    elif nasc % 12 == 4:
        print(signos[4][1])
    elif nasc % 12 == 5:
        print(signos[5][1])
    elif nasc % 12 == 6:
        print(signos[6][1])
    elif nasc % 12 == 7:
        print(signos[7][1])
    elif nasc % 12 == 8:
        print(signos[8][1])
    elif nasc % 12 == 9:
        print(signos[9][1])
    elif nasc % 12 == 10:
        print(signos[10][1]) 
    elif nasc % 12 == 11:
        print(signos[11][1])

decSigno()