while True:
    def conversão(h , m , s):
        h = h * 3600
        m = m * 60
        conversão = h + m + s
        
        return conversão

    h = int(input('hora: '))
    m = int(input('minutos: '))
    s = int(input('segundos: '))

    print(f'conversão: {conversão(h, m, s)}')
    print('-'*30)



    






