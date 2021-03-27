#média
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
media = (n1 + n2 + n3 + n4)/4
print('{}Sua média é {:.1f}{}'.format('\033[1;36m', n1, n2, media, '\033[m'))
if media < 5:
    print('Portando você foi {}REPROVADO{}'.format('\033[4;31m', '\033[m'))
elif 5 <= media < 7:
    print('Você esta em {}RECUPERAÇÃO{}'.format('\033[4;35m', '\033[m'))
else:
    print('Portanto você foi {}APROVADO{}'.format('\033[4;32m', '\033[m'))