#calculando a massa corpórea
m = float(input('\nDigite qual sua massa corpórea: (kg) '))
a = float(input('Digite a sua altua: '))
i = m / (a**2)
print('Seu IMC é {:.1f}'.format(i))
if i < 18.5:
    print('Você esta abaixo do peso')
elif 18.5 <= i < 25:
    print('Você esta no peso ideal')
elif 25 <= i < 30:
    print('Você esta em sobrepeso')
elif 30 <= i < 40:
    print('Você esta obeso')
elif i >= 40:
    print('vc tem obesidade mórbida')
