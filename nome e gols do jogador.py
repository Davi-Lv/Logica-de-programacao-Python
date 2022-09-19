def jogador(j, go):
    if j != '':
        return (f'O jogador {j} fez {go} gols no campeonato.')
    else:
        return (f'O jogador <desconhecido> fez {go} gols no campeonato')
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols:  '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
print(jogador(n, g))