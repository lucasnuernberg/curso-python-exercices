lista = []
cont = 0
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso!')
        cont += 1
    else:
        print(f'O {n} ja foi inserido, valor não foi adicionado novamente.')
    cond = str(input('Quer contitunar[S/N]: ')).strip().upper()[0]
    if cond == 'N':
        break
lista.sort()
print(f'\nOs valores inseridos na lista foram ', end='')
for c, n in enumerate(lista):
    print(n, end=' ')
