matriz = [[], [], []]
print('='*40)
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para posição [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para posição [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para posição [2, {c}]: ')))
print('-'*30)
for valor in matriz[0]:
    print(f'[{valor:^5}]', end='  ')
print()
for valor in matriz[1]:
    print(f'[{valor:^5}]', end='  ')
print()
for valor in matriz[2]:
    print(f'[{valor:^5}]', end='  ')
print('')
print('-'*30)
