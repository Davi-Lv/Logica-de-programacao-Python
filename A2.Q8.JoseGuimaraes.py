print('______________________________________')
print('|              -Quest 8-             |')
print('|           -nota dos alunos-        |')
print('|digite "0" para finalizar o programa|')
print('|____________________________________|')
print('')

while True:
    alunos = int(input('QUANTIDADE DE ALUNOS: '))
    print('')
    if alunos == 0:
        print('PROGRAMA ENCERRADO!!')
        break
    

    reprovados = 0
    final = 0
    aprovado = 0
    media_T = 0
    for i in range(alunos):
        nota1 = float(input('primeira nota: '))
        nota2 = float(input('segunda nota: '))
        media = (nota1 + nota2) / 2
        media_T = media_T + media
        print(f'media: {media:.2f}')
        
        if media <= 2:
            print('-REPROVADO-')
            reprovados = reprovados + 1
        elif 2 < media < 7:
            print('-PROVA FINAL-')
            final = final + 1
        elif media > 7:
            print('-APROVADO-')
            aprovado = aprovado + 1
        print('')
        print(f'alunos adicionadas: {i+1} de {alunos}')
    print(f'-> media: {media_T/alunos}')
    print(f'-> final: {final}')
    print(f'-> aprovados: {aprovado}')
    print(f'-> reprovados: {reprovados}')
    print('-----------------------------')
    print(' ')
    print(' ')
    print(' ')
