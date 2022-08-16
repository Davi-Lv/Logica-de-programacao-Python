print('digite 4 valores')
v = (int(input('valor 1: ')), int(input('valor 2: ')), int(input('valor 3: ')), int(input('valor 4: ')))

print(v)

print(f'vezes em que 9 aparece: {v.count(9)}')
if 3 in v:
    print(f'posição do primeiro 3: {v.index(3)+1}°')
else:
    print('3 não digitado')

print('pares: ',end='')
for n in v:
    if n % 2 == 0:
        print(n, end=' ')

