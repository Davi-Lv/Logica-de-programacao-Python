x = int(input('digite um numero: '))
y = int(input('digite um numero: '))
opcao = int(input('1. +\n2. -\n3. *\n4. /\noperação:'))

def funcao(x, y):
    if opcao == 1:
        print(f'{x} + {y} = {x+y}')
    elif opcao == 2:
        print(f'{x} - {y} = {x-y}')
    elif opcao == 3:
        print(f'{x} * {y} = {x*y}')
    elif opcao == 4:
        print(f'{x} / {y} = {x/y}')
    else:
        print('operação invalida')   
funcao(x, y)