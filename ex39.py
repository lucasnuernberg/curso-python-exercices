from datetime import date
ano = date.today().year
nasc = int(input('\nEm que ano você nasceu? '))
alist = ano - nasc
if alist < 18:
    print('Você tem {} anos então falta {} anos para você se alistar no exercito'.format(alist, 18 - alist))
elif alist > 18:
    print('Você tem {} anos e se alistou para o exercito no ano de {}'.format(alist, nasc + 18))
elif 18 == alist:
    print('Você tem 18 anos e se alistará este ano')
