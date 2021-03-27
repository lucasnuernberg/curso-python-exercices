something = input('Digite algo: ')

print('Qual o tipo primitivo? {}'.format(type(something)))
print('Só tem espaços? {}'.format(something.isspace()))
print('É numérico? {}'.format(something.isnumeric()))
print('É minúscula ? {}'.format(something.islower()))
print('É maiúscula ? {}'.format(something.isupper()))
print('É alfabetico? {}'.format(something.isalpha()))
print('Esta capitalizada? {}'.format(something.istitle()))
