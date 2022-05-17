while True:
    def soma():
        soma = 0
        for i in range(1, n+1):
            soma = soma + i

        return soma

    n = int(input('digite um numero positivo: '))
    if n < 0:
        print('o numero deve ser positivo')
    else:
        print(f'soma dos numeros entre 1 até o numero digitado é igual a: {soma()}')
        print('digite "0" para finalizar')
        print(f'-'*30)
