#ver se o número é primo
from time import sleep
numero = int(input('\nDigite um número: '))
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:  #mostrando que o número é divisível
        print('\033[33m', end=' ')
        cont += 1  #contador de números

    else:
        print('\033[31m', end=' ')

    sleep(0.25)
    print(c, end=' ')
if cont == 2:
    print('\nO número {} foi {} vezes divisível \n{}O NÚMERO É PRIMO'.format(numero, cont, '\033[34m'))
elif numero == 1:
    print('\n{}O número {} tem {} divisor{}'
          '\nPORTANTO NÃO É PRIMO'.format('\033[32m', numero, cont, '\033[m'))
else:
    print('\n{}O número {} tem {} divisores{}'
          '\nPORTANTO NÃO É PRIMO'.format('\033[32m', numero, cont, '\033[m'))
#print('A definição mais comum é que "um número'
     # '\n é primo se for divisível por 1 e '
     # '\npor ele mesmo" ou então "é todo'
     # '\n o número com dois e somente'
     # ' \ndois divisores, ele '
     # 'próprio e a unidade"')
