#analisando triangulo e classificando
n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possível formar um triângulo', end=' ')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    if n1 == n2 and n1 != n3 or n2 == n3 and n2 != n1 or n1 == n3 and n1 != n2:
        print('isóceles')
    if n1 != n2 != n3:
        print('escaleno')
else:
    print('Não é possível foramar um triângulo')



