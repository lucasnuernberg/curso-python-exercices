tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez','onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
         'dezessete', 'desoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Tente novamente: '))
    print(f'O número digitado foi {tupla[n]}')
    cond = str(input('Você quer continuar[S/N]: ').strip().upper()[0])
    if cond == 'N':
        break



