lista = []

for l in range(5):
    lista.append((int(input('digite um valor: '))))

print(lista)
print(f'maior valor {max(lista)} e posição foi {lista.index(max(lista))}')
print(f'menor valor {min(lista)} e posição foi {lista.index(min(lista))}')