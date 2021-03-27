#jogo par ou ímpar
from random import randint
cont = 0
print('\033[31m=~'* 8)
print('\033[32mPar ou Ímpar'.center(22))
print('\033[31m=~'* 8)
while True:
    computador = randint(0, 10)
    #print(computador)
    eu = int(input('\033[34mDigite um número:'))
    soma = eu + computador
    pi = str(input('Par ou Impar[P/I]: ')).strip().upper()[0]
    while pi not in 'PIÍ':                                          #repetir até o usuario iserir o valor certo
        pi = str(input('Par ou Impar[P/I]: ')).strip().upper()[0]
    if pi in 'Pp':
        if soma % 2 == 0:
            print(f'Você ganhou, computador jogou {computador} e a soma deu {soma}')
            cont += 1
        else:
            print('\033[31mVocê perdeu.\033[m')
            break
    elif pi in 'IÍ':
        if soma % 2 == 1:#verificando se é par
            print(f'Você ganhou, computador jogou {computador} e a soma deu {soma}')
            cont += 1
        else:
            print('\033[31mVocê perdeu.\033[m')
            break
    print('='* 20)
print(f'Totalizou {cont} vitórias')

