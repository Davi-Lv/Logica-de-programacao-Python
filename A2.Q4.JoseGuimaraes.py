print('______________________________________')
print('|              -Quest 4-             |')
print('|             -emprestimo-           |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')





while True:
    valor = float(input('valor da casa: R$'))
    salario = float(input('salario: R$'))
    anos = int(input('anos a pagar: '))
    prestação = valor / (anos*12)
    minimo = salario * 30 / 100
    if valor == 0 or salario == 0 or anos == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    elif prestação <= minimo:
        print('emprestimo aprovado')
    else:
        print('emprestimo não foi aprovado')
    print('-------------------')
