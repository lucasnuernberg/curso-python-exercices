from random import randint
from time import sleep
import operator
dicionario = dict()
print('\n---- Valores Sorteados ----')
for c in range(1, 5):
    num = randint(1, 6)
    print(f'Jogador {c}: {num}')
    dicionario[f'Jogador{c}'] = num
    sleep(1)
print('=-'*20)
print('           ---- RANKING ----')
print('=-'*20)
ranking = list()
ranking = sorted(dicionario.items(), key=operator.itemgetter(1), reverse=True)
print(ranking)
for k, v in enumerate(ranking):
    print(f'   {k + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
print(f'{"VOLTE SEMPRE":~^30}')

