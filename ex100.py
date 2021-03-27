import random
from time import sleep
numeros = []
def sorteando(lista):
    for i in range(5):
        n = random.randrange(10)
        lista.append(n)


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos números {numeros} dos números pares é {soma}')

print('')
sorteando(numeros)
print(f'Os números sorteados foram', end=' ')
for num in numeros:
    print(num, end=' ')
    sleep(0.5)
print()
somaPar(numeros)



