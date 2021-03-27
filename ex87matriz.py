#MATRIZ aprimorada
matriz = [[], [], []]
somapar = somafila = 0
print('='*40)
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para posição [0, {c}]: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para posição [1, {c}]: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para posição [2, {c}]: ')))
print('*+='*20)
for valor in matriz[0]:
    print(f'[{valor:^5}]', end=' ')
    if valor % 2 == 0:
        somapar += valor
print()
for i, valor in enumerate(matriz[1]):
    print(f'[{valor:^5}]', end=' ')
    if i == 0:
        maior = valor
    elif valor > maior:
        maior = valor
    if valor % 2 == 0:
        somapar += valor
print()
for valor in matriz[2]:
    print(f'[{valor:^5}]', end=' ')
    if valor % 2 == 0:
        somapar += valor
for valor in matriz:
        somafila += valor[2]
print()
print('*+='*20)
print(f'A soma dos valores da terceira fila é {somafila}')
print(f'O maior valor da segunda coluna é {maior}')
print(f'A soma dos números pares é {somapar}')
