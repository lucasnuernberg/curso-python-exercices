n1 = int(input('\nValor 1:'))
n2 = int(input('Valor 2:'))
n3 = int(input('Valor 3:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O menor valor é {}'.format(menor))
