pessoas = []
dados = []
cont = 0
while True:
    nome = str(input(('Digite um nome: '))).strip().capitalize()
    peso = float(input('Digite seu peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Você quer continuar?[S/N] ')).strip().upper()[0]
    if cond == 'N':
        break
print('='*40)
for i, n in enumerate(pessoas):
    if i == 0:
        pessoame = pessoama = n[0]
        menorp = maiorp = n[1]
    elif n[1] > maiorp:
        pessoama = n[0]
        maiorp = n[1]
    elif n[1] < menorp:
        menorp = n[1]
        pessoame = n[0]
    else:
        if maiorp == n[1]:
            pessoama = pessoama, n[0]
        if menorp == n[1]:
            pessoame = pessoame, n[0]
print(f'O maior peso registrado foi {maiorp:.2f}kg. Peso de {pessoama} ')
print(f'O menor peso registrado foi {menorp:.2f}kg. Peso de {pessoame}')
print(f'Ao todo você castrou {len(pessoas)} pessoas')


