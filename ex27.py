cores = {'amarelo':'\033[33m',
         'vermelho':'\033[31m'}
nome = str(input('Digite seunome completo: ')).title().strip()
lista = nome.split()
n = (len(lista))
print('{}Muito prazer em te conhecer {}!'.format(cores['amarelo'], lista[0]))
print('{}{} eu vi que seu ultimo nome é {} '.format(cores['vermelho'], lista[0], lista[n - 1]))

