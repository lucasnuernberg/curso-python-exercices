v = int(input('\33[7:30mQual a velociade do carro em km/h:'))
if v>80:
    taxa = (v - 80)*7
    print('Você foi multado e deverá pagar R${:.2f}'.format(taxa))
else:
    print('\033[7:30mVocê esta dentro do limite permitido\033[m')
