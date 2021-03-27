from time import sleep
km = float(input('\n{}Quantos km irão ser percorridos : '.format('\033[34m')))
print('Boa viagem!')
print('{}CALCULANDO VALOR A SER PAGO...{}'.format('\033[1;31m', '\033[m'))
sleep(2)
if km <= 200:
    valor = km * 0.50
    print('\033[1;36mO valor a ser pago é de R${:.2f}'.format(valor))
else:
    valor2 = km * 0.45
    print('\033[1;31mValor a ser pago e de R${:.2f}'.format(valor2))
