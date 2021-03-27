from ex109 import moeda
p = float(input('Digite o valor: '))
print(f'O dobro de {p} é {moeda.dobro(p, True)}')
print(f'A metade do valor é {moeda.metade(p, True)}')
print(f'{moeda.moeda(p)} com 15% de aumento fica {moeda.aumentar(p, 15, True)}')
