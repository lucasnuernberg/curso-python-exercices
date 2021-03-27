alunos = []
dados = []
while True:
    print('=' * 20)
    dados.append(str(input('Nome: ').capitalize()))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Notas 2: ')))
    alunos.append(dados[:])
    dados.clear()
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar? ')).strip().upper()[0]
    if cond == 'N':
        break
print('=-'*20)
print(f'{"N":<4}{"NOME":<10}{"MÉDIA":>10}')
print('=-'*20)
for i, c in enumerate(alunos):
    media = 0
    media = (c[1] + c[2])/2
    print(f'{i:<4}{c[0]:<10}{media:>10.1f}')
while True:
    print('='*30)
    notas = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    print('=' * 30)
    if notas < len(alunos):
        print(f'As notas de {alunos[notas][0]} foram {alunos[notas][1]} e {alunos[notas][2]}')
    elif notas == 999:
        break
    else:
        print('Digite um número de aluno válido')
print(alunos)
