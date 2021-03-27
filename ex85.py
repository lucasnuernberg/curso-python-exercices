todos = [[], []]

for c in range(1,8):
    valor = int(input(f'Digite o {c}º numero: '))
    if valor % 2 == 0:
        todos[0].append(valor)
    else:
        todos[1].append(valor)
todos[0].sort()
todos[1].sort()
print(f'Os números PARES são: {todos[0]}')
print(f'Os números ÍMPARES são: {todos[1]}')