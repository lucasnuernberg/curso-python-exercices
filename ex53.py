
#palíndromo
nome = str(input('\nDigite uma frase: ').upper())
n0 = nome.split() #separei a str
sla = ''.join(n0).upper() #juntei a str
n1 = (nome[::-1]) #inverti a str
n2 = n1.split() #separei a str
junto = (''.join(n2)) #juntei a str
print('{}Sua frase {} ao contrário fica {}{}'.format('\033[33m', nome, junto, '\033[m'))
if junto == sla:
    print('{}A frase digita da é um PALÍNDROMO'.format('\033[032m'))
else:
    print('{} não é uma palídromo'.format((nome)).capitalize())


