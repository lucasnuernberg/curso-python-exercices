#lendo peso
print('\033[32m-' * 80)#formatando a estética
print('\033[35mLEITOR DE PESOS'.center(80))
print('\033[31m-\033[m' * 80)
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pessoa)))
    if pessoa == 1:# quando ele receber o peso da primeira pessoa,
                         # vai ler como se fosse o maior e o menor ao mesmo tempo
        maior = peso
        menor = peso
    else:# a partir da segunda pesssoa ele vai rodar esse comando
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('='*30)
print('O maior peso foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

