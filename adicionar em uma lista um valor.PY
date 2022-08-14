lista = []
while True:
    L = int(input('digite um numero: '))
    if L not in lista:
        lista.append(L)
        print('adicionado')
    else:
        print('valor ja adicionado')

    sn = str(input('continuar ? S/N '))
    if sn in 'Nn':
        break

lista.sort()
print(f'numero digitados: {lista}')