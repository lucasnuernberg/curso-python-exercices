#lendo uma tupla
lista = ('Criciuma', 'Fluminense', 'Flamengo', 'Vasco', 'Gremio', 'Inter')
num = len(lista)

print(f'\nO primeiro colocado é {lista[0]}')
print(f'Os três primeiros são {lista[0:3]}')
print(f'Os times em ordem alfabetica {sorted(lista)}')
print(f'Os 2 ultimos colocados são {lista[-2:]}')
pos = lista.index('Flamengo')
print(f'O Flamengo esta na posição {pos+1}')
