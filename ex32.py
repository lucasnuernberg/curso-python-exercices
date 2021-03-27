from datetime import date
ano = int(input('\nDigite um ano e caso quiser o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}{}, ano BISSEXTO'.format('\033[1;31m', ano))
else:
    print('{}{}, ano BISSEXTO'.format('\033[4;34m', ano))
