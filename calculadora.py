print('______________________________________')
print('|            -calculadora-           |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')




#WHILE para entrar em um laço de repetição e TRUE para sempre entrar 
while True:
    
    #criei uma variavel com um INPUT do tipo INTEGER que ira receber o numero digitado pelo usuario 
    operação = int(input('escolha umas das operações\n1. adção\n2. subtração\n3. multiplicação\n4. divisão\n0. finalizar\n'))
    
    #cada numero de 0 (zero) a 4 (quatro) ira fazer uma operação, sendo o 1. adção, 2. subtração 3. multiplicação 4. para divisão e 0. para finalizar
    
    #o valor 0 (zero) ira dar um break para parar o programa
    if operação == 0:  
        print('PROGRAMA ENCERRADO!!')
        break
    print('--------------------')

    #x e y sera os valores digitados para fazer a operação
    x = float(input('valor 1: '))
    y = float(input('valor 2: '))
    
    #logo, criei um IF, se a operação for igual a '1' sera somado os valores e vai imprimir o calculo 
    if operação == 1:
        calculo = x + y
        print(f'adção: {calculo:.2f}')
        
    #elif para continuar, a operação 2 faz um calculo de subtração e já imprimi o valor resultante e assim por diante até chegar o else
    elif operação == 2:
        calculo = x - y
        print(f'subtração: {calculo:.2f}')
    elif operação == 3:
        calculo = x * y
        print(f'multiplicação: {calculo:.2f}')
    elif operação == 4:
        calculo = x / y
        print(f'divisão: {calculo:.2f}')
    #aqui, caso o valor seja diferente de qualquer um das operaçoes, ele vai entrar aqui e imprimir na tela que está invalido
    else:
        print('numero de operação invalida')
    print('--------------------')
