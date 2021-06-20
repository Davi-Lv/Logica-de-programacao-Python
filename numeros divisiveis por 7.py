print('______________________________________')
print('|     -numeros divisiveis por 7-     |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')

while True:
    x = int(input('numero maior: '))
    y = int(input('numero menor: '))
    i = 0
    divisivels = 0
    if x == 0 and y == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    elif x < y:
        print('o primeiro valor deve ser maior que o segundo')
    elif x < 0 or y < 0:
        print('os 2 valores devem ser positivos')
    elif x == y:
        print('os 2 valores devem ser diferentes')
    else:
        print('')
        print('-numeros divisiveis por 7-')
        for i in range(y,x):
            if i % 7 == 0:   
                divisivels = divisivels + 1    
                print(f'-> {i} <-')
        print('')
        print(f'total de divisiveis: {divisivels}')
    print('----------------------')
    print('')
