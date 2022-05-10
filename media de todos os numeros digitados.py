x = []
while True:
    x.append(int(input('digite um numero: ')))
    stop = str(input('continuar? [S/N]'))
    if stop in 'Nn':
        break

def soma(x):
    soma = 0
    for i in x:
        soma = soma + i
        print(soma)
    print(soma/len(x))
    
soma(x)