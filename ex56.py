idadetotal = 0
idademaisvelho = 0
nomemaisvelho = ''
mulheres20 = 0
for p in range(1, 5):
    print('-' * 15,'{}° PESSOA'.format(p), '-' * 15)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    idadetotal += idade
    if p == 1 and sexo in 'Mm':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > idademaisvelho:
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade < 20 and sexo in 'Ff':
        mulheres20 += 1

media = idadetotal/p

print('='*30)

print('A média de todos as idades das {} pessoas é {:.2f} anos'.format(p, media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomemaisvelho, idademaisvelho))
print('O número de mulheres com menos de 20 anos é {}'.format(mulheres20))






