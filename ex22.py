
nome = str(input('\nDigite seu nome completo: '))
print('='*40)
print('Seu nome em maiúsclo ficaria: {}'.format(nome.upper()))
print('Seu nome em minúsculo ficaria: {}'.format(nome.lower()))

n1 = nome.split() #Aqui eu separei o nome em uma lista
print('Seu nome tem {} letras'.format(len(''.join(n1))))
print('Seu primeiro nome tem {} letras'.format(len(n1[0])))
print('Essa é a lista que fiz para unir seu nome como fiz abaixo: {}'.format(n1))
print(f'Seu nome sem espaços: {"".join(n1)}')
print('='*40)


