#Pintando uma parede
print('-'*60)
altura = float(input('Informe a altura em metros da parede que você deseja pintar: '))
largura = float(input('Informe a largura em metros da parede que você deseja pintar: '))

area = altura * largura

#1L - 2m²
#20 - 40

quantTinta = area / 2

print('A quantidade de tinta necessária é {:.1f}L'.format(quantTinta))
print('-'*60)