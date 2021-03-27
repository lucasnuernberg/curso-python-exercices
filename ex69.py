#cadastro de pessoas
cont_m = cont_a = cont_f = 0
while True:
    age = int(input('\nIdade: '))
    if age >= 18:
        cont_a += 1
    sex = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if sex in 'M':
        cont_m += 1
    elif sex in 'F' and age < 18:
        cont_f += 1
    while sex not in 'MF':
        sex = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if sex in 'M':
            cont_m += 1
        elif sex in 'F' and age < 18:
            cont_f += 1
    continuar = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Digite somente[S/N]: ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    print('~=' * 10)

print('~=' * 15)
print(f'Foram cadastrados {cont_m} homens')
print(f'Foram cadastradas {cont_a} pessoas com mais de 18 anos')
print(f'Foram cadastradas {cont_f} meninas com menos de 18 anos')
