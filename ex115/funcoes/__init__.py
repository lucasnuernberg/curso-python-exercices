from ex115.cabeca import *
from time import sleep

def criararq(file):
    try:
        open(file, 'rt')
    except:
        open(file, 'wt+')
        print('criado')

def lerarq(file):
    try:
        a = open(file, 'rt')
    except:
        print('houve um erro')
    else:
        alinhar('PESSOAS CADASTRADAS')

        for i, item in enumerate(a):
            dado = item.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{i} - {dado[0]:<30}{dado[1]:>2} anos')



def adicionar(arq, nome='', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao adicionar')
    else:
        try:
            a.write(f'{nome};{idade}\n')

            a.close()
        except:
            print('ERRou merda')
        else:
            print(f'Cadastrando {nome}...')
            sleep(1)
            print('Cadastro completo')
            sleep(0.7)

def retirar(arq, ret=0):
    a = open(arq, 'rt')
    print(a)

