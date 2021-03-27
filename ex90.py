dicio = {}
dicio['Nome'] = str(input('Nome: '))
dicio['Média'] = float(input(f'Qual a média de {dicio["Nome"]}: '))
if dicio['Média'] >= 7:
    dicio['Situação'] = 'APROVADO!'
elif 7 > dicio['Média'] >= 5:
    dicio['Situação'] = 'RECUPERAÇÃO'
else:
    dicio['Situação'] = 'REPROVADO'
print('=-'*20)
for k, v in dicio.items():
    print(f'--> {k} é igual a {v}')

