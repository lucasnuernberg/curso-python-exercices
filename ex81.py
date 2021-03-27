lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer cotinuar:[S/N] ')).strip().upper()[0]
    print('=' * 15)
    if cond == 'N':
        break
print('=-'*50)
print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'A lista de forma decrescente {lista}')
if 5 in lista:
    print('O número 5 foi encontrado na lista')
else:
    print('O número 5 não foi encontrado na lista')
