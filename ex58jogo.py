import random
from time import sleep

cont = 1
computador = random.randint(0, 10)#fazendo computador pensar em um número
print('{}='.format('\033[0;33m')*30)

n = int(input('\nDigite um número entre 0 e 10:{} '.format('\033[m')))
print('PROCESSANDO...')

sleep(1)
while computador != n:#condição para perguntar novamente
    if computador > n:
        n = int(input('Hmm... Tente um valor maior: '))
    elif computador < n:
        n = int(input('Hmm... Tente um valor menor: '))
    cont += 1

if computador == n:
    if cont > 1:
        print('>>> Acertou usando {} tentativas'.format(cont))
    else:
        print('acertou usando 1 uma tentativa')





