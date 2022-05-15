tab = []
apro = 0
repro = 0
alunos = int(input('Digite o número de alunos: '))
for i in range(alunos):
    aluno = []
    nome = input('Digite o nome do aluno:')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    med = (n1 + n2)/2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(med)
    if med >= 6:
        apro += 1
    else:
        repro += 1
    tab.append(aluno)
print(tab)
print(f'A quantidade de alunos aprovados foi de {apro}, e a quantidade de alunos reprovados foi de {repro}')