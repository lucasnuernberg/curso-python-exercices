from time import sleep
futebol = dict()
listgols = list()
total = 0
futebol['Jogador'] = str(input('Nome: ')).strip().title()
partidas = int(input(f'Quantas partidas {futebol["Jogador"]} jogou? '))
print('-='*30)
for i in range(1, partidas + 1):
    gol = int(input(f'Quantos gols na partida {i}: '))
    listgols.append(gol)
    total += gol
futebol['gols'] = listgols[:]
sum(listgols)#soma as valores da lista
futebol['total'] = total
print('-='*30)
for k, v in futebol.items():
    print(f'O valor de {k} é {v}')
print('-='*30)
print(f'O jogador {futebol["Jogador"]} jogou {len(futebol["gols"])} partidas'.center(30))
for p, g in enumerate(listgols):
    print(f'  ---> Na partida {p + 1}---> marcou {g} gols')
    sleep(1)
print(f'Totalizando {futebol["total"]} gols')




