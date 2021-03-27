#pedra papel tesoura
import random
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print('{}JOKENPO{}'.center(110).format('\033[1;36;42m', '\033[m'))
print('PAPEL[1]')
print('PEDRA[2]')
print('tesoura[3]')
eu = int(input('ESCOLHA PEDRA PAPEL TESOURA: '))

if eu == 1 and computador == 'pedra':
    print('VOCÊ VENCEU')
elif eu == 1 and computador == 'papel':
    print('empate')
elif eu == 1 and computador == 'tesoura':
    print('computador venceu')
elif eu ==2 and computador == 'papel':
    print('computador ganhou')
elif eu == 2 and computador == 'pedra':
    print('empate')
elif eu == 2 and computador == 'tesoura':
    print('vc ganhou')
elif eu == 3 and computador == 'papel':
    print('vc ganhou')
elif eu == 3 and computador == 'pedra':
    print(' pc won')
elif eu == 3 and computador == 'tesoura':
    print('empate')
print('o computador escolheu {}'.format(computador))


