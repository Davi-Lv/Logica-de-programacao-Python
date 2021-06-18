print('______________________________________')
print('|            -calculadora-           |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')





while True:
    operação = int(input('escolha umas das operações\n1. adção\n2. subtração\n3. multiplicação\n4. divisão\n0. cancela\n'))
    if operação == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    print('--------------------')

    x = float(input('valor 1: '))
    y = float(input('valor 2: '))
    if operação == 1:
        calculo = x + y
        print(f'adção: {calculo:.2f}')
    elif operação == 2:
        calculo = x - y
        print(f'subtração: {calculo:.2f}')
    elif operação == 3:
        calculo = x * y
        print(f'multiplicação: {calculo:.2f}')
    elif operação == 4:
        calculo = x / y
        print(f'divisão: {calculo:.2f}')
    else:
        print('numero de operação invalida')
    print('--------------------')
