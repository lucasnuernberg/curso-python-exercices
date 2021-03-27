#informando a categoria dos nadadores
import datetime
nasc = int(input('Em quem ano você nasceu? '))
idade = datetime.date.today().year - nasc

if idade <= 9:
    print('{}Você tem {} anos então sua categoria é mirim{}'.format('\033[1;34m', idade, '\033[m'))
elif 9 < idade <= 14:
    print('{}Você tem {} anos então sua categoria é INFANTIL{}'.format('\033[1;34m', idade, '\033[m'))
elif 14 < idade <=19:
    print('{}Você tem {} anos então sua categoria é JUNIOR{}'.format('\033[1;34m', idade, '\033[m'))
elif 19 < idade <= 25:
    print('{}Você tem {} anos então sua categoria é SENIOR{}'.format('\033[1;34m', idade, '\033[m'))
elif 25 < idade:
    print('{}Você tem {} anos então sua categoria é MASTER{}'.format('\033[1;34m', idade, '\033[m'))

