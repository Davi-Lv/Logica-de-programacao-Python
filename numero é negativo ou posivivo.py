while True:
    def result(x):
        if x > 0:
            print('numero positivo')
        else:
            print('numero negativo')
        print('-'*30)

    x = int(input('digite um numero: '))
    result(x)