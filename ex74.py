#gerando números aleatórios
import random
print('')
n1 = random.randrange(10)
n2 = random.randrange(10)
n3 = random.randrange(10)
n4 = random.randrange(10)
n5 = random.randrange(10)
lista = (n1, n2, n3, n4, n5)
print(f'Os valores são: ', end='')
for n in lista:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {min(lista)}')
print(f'O menor valor sorteado foi {max(lista)}')
print(lista)
#print(f'O primeiro dessa lista é {embaralhado[0]} e o ultimo é {embaralhado[-1]}')

