print('______________________________________')
print('|              -Quest 2-             |')
print('|           -novo salario-           |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')



while True:
    salario = float(input('salario atual: R$'))
    
    if salario < 0:
        print('não pode ser um numero negativo')
    elif salario == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    elif salario <= 500:
        total = (salario*0.05)+salario+150
        print('bonificação: 5%')
        print('auxilio escola: R$150')
        print(f'salario total: R${total:.2f}')
    elif 501 <= salario <= 600 :
        total = (salario*0.12)+salario+150
        print('bonificação: 12%')
        print('auxilio escola: R$150')
        print(f'salario total: R${total:.2f}')  
    elif 601 <= salario <= 1200:
        total = (salario*0.12)+salario+100
        print('bonificação: 12%')
        print('auxilio escola: R$100')
        print(f'salario total: R${total:.2f}')  
    elif salario >= 1201:
        total = salario+100
        print('bonificação: não')
        print('auxulio escola: 100')
        print(f'salario total: {total}')
    print('------------------')