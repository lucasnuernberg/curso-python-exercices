from time import sleep
q = 0
n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('Segundo valor: '))
while q != 5:
    print('=' * 30)
    print(' ' * 4, '[1] somar')
    print(' ' * 4, '[2] multiplicar')
    print(' ' * 4, '[3] maior')
    print(' ' * 4, '[4] novos número')
    print(' ' * 4, '[5] sair do programa')
    q = int(input('>>>>Digite a operação que deseja realizar: '))
    while q <= 0 or q >= 6: #condição para pedir novo valor caso a opção escolhida
        q = int(input('Valor inválido, digite novamente: '))#não esteja dentro dos valores
    if q == 1: #condiçao para mostrar maior valor
        print('>>A soma de {} + {} é {}'.format(n1, n2, n1 + n2))
    elif q == 2:
        print('>>O produto de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif q == 3:
        if n1 > n2:
            print('>>O maior número é', n1)
        else:
            print('>>O maior número é', n2)
    elif q == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    sleep(1)
sleep(1)
print('Finalizando...')
sleep(1)
print('=' * 30)
print('Fim do programa')

