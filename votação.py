def voto(ano):
    from datetime import date
    ano = date.today().year
    idade = ano - nascimento
    if idade >= 16 and idade < 18 or idade > 65:
        return print(f'Com {idade} anos: o voto é opcional.')
    elif idade < 16:
        return print(f'Com {idade} anos: o voto não é permitido.')
    elif idade > 18:
        return print(f'Com {idade} anos: o voto é obrigatório.')

nascimento = int(input('Digite o ano de nascimento: '))
voto(nascimento)