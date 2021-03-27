#Soma de todos números ímpares e múltiplos de 3 entre 1 e 500
soma = 0
cont = 0
for c in range(3, 501, 6):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('Os {} números dentro dessa variável somam {}'.format(cont, soma))


