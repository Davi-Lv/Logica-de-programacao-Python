numeros = ('zero', 'um', 'dois', 'três','quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    x = int(input("Qual o número: "))
    if 0 <= x <= 20:
        print(f"{x} - {numeros[x]}")
    else:
        print(f"Digite um número entre 0 e 20!")
