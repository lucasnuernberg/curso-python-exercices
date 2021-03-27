countmax = countmin = 0
num = list()
for n in range(0, 5):
    num.append(int(input(f'Digite um número na posição {n}: ')))
print(f'\nA lista é{num}')
print(f'O maior valor foi {max(num)} e foi digitado na posição', end=' ')
for c, v in enumerate(num):
    if v == max(num):
        print(c, end=' ')
print(f'\nO menor valor foi {min(num)} e foi digitado na posição', end=' ')
for co, va in enumerate(num):
    if va == min(num):
        print(co, end=' ')
