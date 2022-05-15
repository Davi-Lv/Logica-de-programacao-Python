gab = ('A', 'C', 'E', 'B', 'D', 'B', 'B', 'C', 'A', 'E')
tab = []
while True:
    aluno = []
    resposta = []
    nota = 0
    nome = input('Digite o nome do aluno(digite /stop para parar): ')
    if nome == '/stop':
        break
    aluno.append(nome)
    for i in range(len(gab)):
        q = input(f'Digite a resposta da questão {i+1}: ')
        while q.upper() not in gab:
            q = input(f'ERRO! Digite a resposta da questão {i + 1}: ')
        if q.upper() == gab[i]:
            nota = nota + 1
        resposta.append(q.upper())
    aluno.append(resposta)
    aluno.append(nota)
    tab.append(aluno)
for g in range(len(tab)):
    print(f'O aluno {tab[g][0]} acertou {tab[g][2]}')