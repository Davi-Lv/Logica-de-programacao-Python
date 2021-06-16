
total = 0
while True:
    codigo = int(input('escolha os codigos dos produtos\n1. R$5,00\n2. R$8,00\n3. R$10,00\n4. R$13,00\n5. R$16,00\n0. total.\n'))
    if codigo == 0:
        print(f'total = R${total:.2f}')
        break
    elif 1 <= codigo <= 3 or codigo == 5 or codigo == 9:
        quantidade = int(input('qual a quantidade: '))
        if codigo == 1:
            total = total + quantidade * 5
        elif codigo == 2:
            total = total + quantidade * 8
        elif codigo == 3:
            total = total + quantidade * 10
        elif codigo == 4:
            total = total + quantidade * 13
        elif codigo == 5:
            total = total + quantidade * 6
    else:
        print('codigo invalido')
        break
