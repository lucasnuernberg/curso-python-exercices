n = int(input('Digite um número: '))
r = int(input(('Razão: ')))
c = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while total > c:
        print(n, '> ', end='')
        n += r
        c = c + 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja visualizar: (0 para parar) '))
print('Foram exibidos na tela {} termos.'.format(total))

