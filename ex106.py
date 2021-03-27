#continuar com as frescuras a mais
def ajuda():
    while True:
        n = str('_-' * 15)
        print(f'\033[1:43:36m{n.center(100)}')
        print('Sistema de ajuda'.center(100))
        print(n.center(100))
        h = input('\033[mFunção ou biblioteca-->')
        if h.lower() == 'fim':
            break
        print('\033[7;30m')
        help(f'{h}')


ajuda()