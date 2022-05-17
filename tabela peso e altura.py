print('______________________________________')
print('|              -Quest 3-             |')
print('|        -tabela peso e altura-      |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')





while True:
    altura = float(input('altura em cm: '))
    peso = float(input('peso em kg: '))

    if altura == 0 or peso == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    elif altura <= 119:
        if peso <= 60:
            print('tipo "A"')
        elif 60 <= peso <= 90:
            print('tipo "D"') 
        elif peso > 90:
            print('tipo "G"')

    elif 120 <= altura <= 170:
        if peso <= 60:
            print('tipo "B"')
        elif 60 <= peso <= 90:
            print('tipo "E"')
        elif peso > 90:
            print('tipo "H"')
    elif altura > 170:
        if peso <= 60:
            print('tipo "C"')
        elif 60 < peso < 90:
            print('tipo "F"')
        elif peso > 90:
            print('tipo "I"')
    print('-------------------')
