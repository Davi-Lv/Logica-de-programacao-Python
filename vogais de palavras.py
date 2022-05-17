def vogais(lst):
    for i in lst:
        vogal = ""
        palavra = i
        for x in range(len(palavra)):
            if palavra[x] == "A" or palavra[x] == "E" or palavra[x] == "I" or palavra[x] == "O" or palavra[x] == "U":
                vogal += f"{palavra[x]} "
        print(f"as vogais da palavra {i} são ( {vogal}) ")

palavras = ('TELEVISÃO', 'COMPUTADOR', 'CELULAR', 'GARRAFA', 'PORTA', 'MUSICA', 'MESA', 'CADEIRA')
vogais(palavras)
