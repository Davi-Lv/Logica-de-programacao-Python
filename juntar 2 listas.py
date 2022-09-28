pessoa1 = []
pessoa2 = []


pessoa1 = str(input('oque faz no tempo livre? '))
pessoa2 = str(input('oque faz no tempo livre? '))


if pessoa1 in pessoa2:
    print(pessoa1, pessoa2)

print(f'a primeira pessoa gosta de: {pessoa1} e a segunda pessoa gosta de: {pessoa2}')