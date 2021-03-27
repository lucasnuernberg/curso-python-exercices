#formatando
print('')
compras = ('Lápis', 2.50,
           'Borracha', 4,
           'Penal',12.50,
           'Caderno',14.80,
           'Lapiseira', 12.50)
for n in range(0, len(compras)):
    if n % 2 == 0:
        print(f'{compras[n]:.<30}', end=' ')
    else:
        print(f'R${compras[n]:.2f}')