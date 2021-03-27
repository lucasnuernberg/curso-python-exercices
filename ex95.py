
tjoga = []
futebol = dict()
listgols = list()
while True:
    futebol['Jogador'] = str(input('\nNome: ')).strip().title()
    partidas = int(input(f'Quantas partidas {futebol["Jogador"]} jogou? '))
    print('-='*20)
    for i in range(1, partidas + 1):
        gol = int(input(f'Quantos gols na partida {i}: '))
        listgols.append(gol)
    futebol['gols'] = listgols[:]
    sum(listgols)#soma as valores da lista
    futebol['total'] = sum(listgols)#soma as valores da lista
    tjoga.append(futebol.copy())
    futebol.clear()
    listgols.clear()
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if cond not in 'SN':
            print('Por favor, digite somente SIM ou NÃO!')
    print('=-' * 20)
    if cond == 'N':
        break
print(f'{"cod":<5}{"nome":<10}{"gols":<20}{"total":<10}')
print('=-'*30)
for i, p in enumerate(tjoga):
    print(f'{i:<5}{p["Jogador"]:<10}{str(p["gols"]):<20}{p["total"]:<10}')
print('=-'*30)

while True:
    cont = 0
    dados = int(input('Quer ver os dados de qual jogador: '))

    if dados == 999:#999 para sair
        break
    elif dados >= len(tjoga):
        print('Selecione um jogador válido')
    else:
        print(f' Levantamento do jogador {tjoga[dados]["Jogador"]}')
        for jo in tjoga[dados]['gols']:
            print(f'    {cont + 1}º partida ---> {jo} gols')
            cont += 1
print(f'{"VOLTE SEMPRE":=^30}')
