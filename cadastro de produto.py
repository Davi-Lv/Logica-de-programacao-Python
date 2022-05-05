
produtos = []
compravenda = []
while True:
    precos = []
    pdt = input('Digite o nome do produto(Digite /stop para parar): ')
    while len(pdt) >= 10:
        pdt = input('Erro,máximo 10 caracteres. Digite o nome do produto(Digite /stop para parar): ')
    if pdt == '/stop':
        break
    produtos.append(pdt)
    prcc = float(input('Digite o valor de compra: '))
    prcv = float(input('Digite o valor de venda: '))
    precos.append(prcc)
    precos.append(prcv)
    compravenda.append(precos)
while True:
    print(','.join(produtos))
    pes = input('Digite o produto a ser calculado(Digite /stop para parar): ')
    if pes == '/stop':
        break
    if pes not in produtos:
        pes = input('Erro,esse produto não consta no banco de de dados. Digite o produto a ser calculado(Digite /stop '
                    'para parar): ')
    print(f'O produto {pes} tem um lucro de R$'
          f'{compravenda[produtos.index(pes)][1]-compravenda[produtos.index(pes)][0]:.2f}')
