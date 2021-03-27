#Mostra 9 termos seguintes com while
num = int(input('Digite um número: '))
razao = int(input(('Razão: ')))
cont = 10
while cont > 0:
    print(num, '> ', end='')
    num += razao
    cont = cont - 1
print('fim')
