sal = float(input('Qual o seu salário atual: R$'))
cores = {'amarelo': '\033[33m',
         'verde': '\033[32m'}
if sal <= 1250:
    print('{}Com o reajuste salárial você passará a receber R${:.2f}'.format(cores['amarelo'], sal*1.15))
else:
    print('{}Com o reajuste salárial você passará a receber R${:.2f}'.format(cores['verde'], sal*1.10))
