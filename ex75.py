cont = 0
n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
lista = (n1, n2, n3, n4)
if lista.count(9) == 0 or lista.count(9) > 1:
    print(f'\nO número 9 apareceu {lista.count(9)} vezes')
else:
    print(f'\nO número 9 apareceu {lista.count(9)} vez')
if lista.count(3) > 0:
    if lista.count(3) == 1:
        print(f'O número 3 foi digitado {lista.count(3)} vez')
    else:
        print(f'O número 3 foi digitado {lista.count(3)} vezes')
else:
    print('O número 3 não foi digitado')
if lista.count(8) > 0:
    print(f'O número 8 apareceu na posição {lista.index(8) + 1}')
else:
    print('O número 8 não apareceu na lista')

print('Os valores pares digitados foram', end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
        cont += 1

print(f'\nApareceram {cont} números pares')
