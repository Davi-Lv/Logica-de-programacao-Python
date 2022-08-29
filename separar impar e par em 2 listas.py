lista = []
par = []
impar = []
while True:
    lista.append(int(input('digite um valor: ')))

    sn = str(input('continuar ? S/N '))
    if sn in 'Nn':
        break

for i, p in enumerate(lista):
    if p % 2 == 0:
        par.append(p)
    elif p % 2 == 1:
        impar.append(p)

print(f'pares: {par}')
print(f'impares: {impar}')
print(f'todos os numeros: {lista}')