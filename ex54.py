#Lendo idades
from datetime import date
contador = 0
menor = 0
data = date.today().year#pego o ano atualizado

for c in range(0, 7): #faço acontecer 6 VEZES a pergunta dentro do laço
    n = int(input(('Em que ano você nasceu: ')))
    if (data - n) >= 18:
        contador += 1
    else:
        menor += 1
if contador == 1:
    n1 = 'pessoa é maior'

else:
    n1 = 'são maiores'
if menor == 1:
    n2 = 'pessoa é menor'
else:
    n2 = 'pessoas são menores'

print('{}{} {} de idade \nE {} {} de 18 anos{}'
      .format('\033[31m', contador, n1, menor, n2, '\033[m'))


