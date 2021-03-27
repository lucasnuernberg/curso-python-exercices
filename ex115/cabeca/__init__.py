from time import sleep
cores = {'vermelho': '\033[31m',
         'azul': '\033[1:34m',
         'verde': '\033[1;92m',
         'inverte': '\033[;7m',
         'zera': '\033[m'
         }
def alinhar(txt):
    print(f'{cores["vermelho"]}-{cores["zera"]}'*42)
    print(f'{cores["azul"]}{txt}'.center(50))
    print(f'{cores["vermelho"]}-{cores["zera"]}'*42)

def leiaint():
    while True:
        try:
            num = int(input('Digite um a sua opção: '))
            sleep(0.5)
        except(ValueError, TypeError):
            print('\033[31mErro, digite um número válido\033[m')
            continue
        else:
            return num

def leiaidade():
    while True:
        try:
            num = int(input('idade: '))
        except(ValueError, TypeError):
            print('\033[31mErro, digite um número válido\033[m')
            continue
        else:
            return num

def num():
    while True:
        try:
            num = int(input('Número da pessoa a ser removida: '))
        except(ValueError, TypeError):
            print('\033[31mErro, digite um número válido\033[m')
            continue
        else:
            return num


def cab(lista):
    print()
    print(f'{cores["vermelho"]}-{cores["zera"]}'*42)
    print(f'{cores["azul"]}MENU'.center(50))
    print(f'{cores["vermelho"]}-{cores["zera"]}'*42)
    num = 1
    for i in lista:
        print(f'{cores["verde"]}{num}{cores["zera"]}', '-', f'{cores["azul"]}{i}{cores["zera"]}')
        num += 1
    print(f'{cores["vermelho"]}-{cores["zera"]}'*42)
    return leiaint()

