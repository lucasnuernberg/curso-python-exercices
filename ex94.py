listat = []
pessoas = {}
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoas['idade'] = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('Por favor, digite somente M ou F!')
    pessoas['sexo'] = sexo
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if cond not in 'SN':
            print('Por favor, digite somente SIM ou NÃO!')
    listat.append(pessoas.copy())
    pessoas.clear()
    if cond == 'N':
        break
print('-='*20)
print(f'--> O grupo tem {len(listat)} pessoas')
for c in listat:
    soma += c['idade']
media = soma/len(listat)
print(f'--> A média das idades é {media:.2f} anos')
print('--> As mulher cadastradas foram:', end=' ')
for m in listat:
    if m['sexo'] == 'F':
        print(m['nome'], end=' ')
print()
print('--> Lista de pessoas acima da média: ')

for ac in listat:
    if ac['idade'] > media:
        for i, v in ac.items():
            print(f'{i} = {v}', end='; ')
        print()
