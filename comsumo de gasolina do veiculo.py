carros = []
comsumo = []


while True:
    carros.append(str(input('nome do carro: ')))
    comsumo.append(float(input('km por litro de gasolina: ')))

    stop = str(input('continuar? (S/N)')).upper()[0]
    if stop in "Nn":
        break

Carmaior = comsumo.index(max(comsumo))
Carmenor = comsumo.index(min(comsumo))



print(f'-maior comsumo-\ncarro: {carros[Carmaior]}\ncomsumo: {max(comsumo)}')
print()
print(f'-menor comsumo-\ncarro: {carros[Carmenor]}\ncomsumo: {min(comsumo)}')
print()
for i in range(len(comsumo)):
    print(f'o carro {carros[i]} gasta {comsumo[i]*1000} litros para Mil km rodados')