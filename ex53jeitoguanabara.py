#jeito guanabara
frase = str(input('Digite uma frase : '.upper()))
cont = ''
n1 = frase.split()
junto = ''.join(n1)
inverso = len(junto)
for letra in range(inverso - 1, - 1, -1):
    cont += junto[letra]
if cont == junto:
    print('palíndromo')
else:
    print('nao é palídromo')






