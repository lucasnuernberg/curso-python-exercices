import random
from time import sleep
r = random.randint(0, 5)
print('='*30)
n = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO')
if r == n:
    print('Parabéns você acertou o número sorteado!!')
else:
    print('Errouuuu, talvez na próxima :(')
    print(r)
print('='*30)
