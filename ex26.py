frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra A esta na posição {}'.format(frase.find('a')+1))
print('A ultima letra A esta na prosição {}'.format(frase.rfind('a')+1))

