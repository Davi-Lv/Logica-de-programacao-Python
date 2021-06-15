print('=================')
print('  caixa poupaça  ')
print('=================')

deposito = float(input('deposito inicial: '))
juros = int(input('taxa de juros: '))
meses = int(input('digite o mes: '))

mes = 1
total = deposito
while mes <= meses:
    deposito = deposito + (deposito * (juros / 100))
    print(f"rendimento mês {mes} é de R${deposito:.2f}.")
    mes = mes + 1
print(f" a poupança rendera: R${(deposito-total):.2f}.")
