#lista par e ímpar
num = list()
pares = list()
impar = list()
while True:
    num.append(int(input('Digite um valor: ')))

    cond = ' '
    while cond not in 'SN':
        cond = str(input('Você quer continuar?[S/N] ')).strip().upper()[0]

    if cond == 'N':
        break
for v in num: #le número por número e jpga pra uma lista
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print(f'\nA lista de números que você digitou foi essa: {num}')
print(f'A lista de números PARES que você digitou foi essa: {pares}')
print(f'A lista de números ÍMPARES que você digitou foi essa: {impar}')

