from datetime import date
ano = date.today().year
dici = dict()
dici['nome'] = str(input('Digite o seu nome: ')).strip().title()
dici['nascimento'] = int(input('Ano de nascimento: '))
dici['idade'] = ano - dici['nascimento']
dici['ctps'] = int(input('Qual seu CTPS: '))
print('')
if dici['ctps'] > 0:
    contratação = int(input('Ano de contratação: '))
    dici['aposentaria'] = 35 - (ano - contratação) + dici['idade']
    dici['salário'] = float(input('Qual salário: '))
for k, v in dici.items():
    print(f'O {k} tem valor de {v}')
