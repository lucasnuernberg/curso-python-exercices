

perg = str(input('Qual seu sexo[M/F]: ')).upper().strip()[0]
while perg not in 'MF':
        perg = str(input('Digite novamente: ')).upper().strip()[0]
print('Sexo {} cadastrado'.format(perg[0]))









