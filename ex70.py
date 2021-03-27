soma = mais = maisba = 0
print('\033[31m=\033[m'*20)
print('Loja do Quilunhas')
print('\033[31m=\033[m'*20)
nomemb = ' '
n = 1
while True:
    print('^~'*12)
    nomep = str(input('Qual nome do produto:')).strip()
    price = float(input('Preço: R$'))
    if n == 1 or price < maisba: #se for o primeiro ou se o preço for menor que o mais barato ele muda
        maisba = price
        nomemb = nomep        #simplificar essas condiçôes
    n += 1
    if price > 1000:
        mais += 1
    soma += price
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if cond == 'N':
        break
print('{:-^40}'.format('Fim Do Programa'))
print(f'A soma de todos produtos foi R${soma}')
print(f'{mais} produtos custam mais de R$1000.00')
print(f'O produto mais barato é {nomemb} e custou R${maisba:.2f}')