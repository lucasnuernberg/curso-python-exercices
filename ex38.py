
n1 = int(input('\nDigite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O maior valor é {}'.format(n1))
elif n2 > n1:
    print('O maior valor é {}'.format(n2))
elif n1 == n2:
    print('os 2 números são iguais')