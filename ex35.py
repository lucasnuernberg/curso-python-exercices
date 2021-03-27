#analisando triângulos
a = float(input('Primeiro cateto em cm: '))
b = float(input('Segundo cateto em cm: '))
c = float(input('Terceiro cateto em cm: '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('É prossivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo ')
