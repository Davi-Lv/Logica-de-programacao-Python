def area(largura, comprimento):
    a2 = largura*comprimento
    print(f'O terreno tem {a2:.2f}m de área')

largura = float(input("largura: "))
comprimento = float(input("comprimento: "))
area(largura, comprimento)