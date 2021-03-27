def cadastro(nome='<desconhecido>', gols=0):
    """
    :param nome:
    :param gols: numero de gols
    :return:
    """
    print(f'O jogador {nome} marcou ({gols}) gol(s) na partida')


n = str(input('Qual nome do jogador: '))
g = str(input(f'Quantos gols {n} marcou: '))
if n.strip() == '':
    if g.isdecimal():
        cadastro(gols=g)
    else:
        cadastro()
else:
    if g.isdecimal():
        cadastro(n, g)
    else:
        cadastro(n)
