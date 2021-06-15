print('______________________________________')
print('|              -Quest 1-             |')
print('|          -nome dos meses-          |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')


while True:
    mes = int(input('Digite o numero do mês: '))
    if mes == 1:
        print('janeiro')
    elif mes == 2:
        print('fevereiro')
    elif mes == 3:
        print('março')
    elif mes == 4:
        print('abril')
    elif mes == 5:
        print('maio')
    elif mes == 6:
        print('junho')
    elif mes == 7:
        print('julho')
    elif mes == 8:
        print('agosto')
    elif mes == 9:
        print('setembro')
    elif mes == 10:
        print('outubro')
    elif mes == 11:
        print('novembro')
    elif mes == 12:
        print('dezembro')
    elif mes == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    else:
        print(f'numero {mes:.0f} invalido')
    print('---------------------------')
    