print('______________________________________')
print('|    -soma de 2 numeros inteirios    |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')

while True:
    x = int(input('valor 1: '))
    if x == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    y = int(input('valor 2: '))
    if y == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    if x < y:
        print('o primeiro valor deve ser maior que o segundo')
    elif x < 0 or y < 0:
        print('os 2 valores devem ser positivos')
    else:
        soma = x+y
        print(f'soma dos valores = {soma}')
    print('----------------------')
    
