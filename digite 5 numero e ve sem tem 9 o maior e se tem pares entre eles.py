def num(n):
    lst = []
    for i in range(n):
        lst.append(int(input("Qual o numero: ")))
    return tuple(lst)


def repete(lst, n):
    s = 0
    for i in lst:
        if i == n:
            s += 1
    return s


def pares(lst):
    npar = []
    for i in lst:
        if i % 2 == 0:
            npar.append(i)
    return npar


numeros = num(4)
print(f"Os números são: {numeros}")
print(f"A) O número 9 apareceu {repete(numeros, 9)} vezes")
try:
    print(f"B) O primeiro 3 apareceu na posição {numeros.index(3) + 1}")
except ValueError:
    print(f"B) Não tem número {3}")
print(f"C) Os números pares são: {pares(numeros)}")
