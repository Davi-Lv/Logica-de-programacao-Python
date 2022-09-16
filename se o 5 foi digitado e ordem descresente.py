lista = []
while True:
    lista.append(int(input('digite um valor: ')))
    sn = str(input('continuar ? S/N '))
    if sn in 'Nn':
        break

if 5 in lista:
    print('o 5 foi digitado')
else:
    print('o 5 não esta na lista')

print(f'elementos: {len(lista)}')

lista.sort(reverse=True)
print(f'ordem descresente: {lista}')