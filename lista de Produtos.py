produtos = ('Teclado', 30,'Mouse', 25, 'Tela', 150, 'Pen-Drive', 60, 'Mouse-Pad', 20)

P = produtos

print('      -lista de Produtos-')

for n in range(len(P)):
    if n % 2 == 0:
        print(f'{P[n]:.<20}', end='')
    else:
        print(f'R$ {P[n]:.2f}')