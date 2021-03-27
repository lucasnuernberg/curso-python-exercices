def area(largura, altura):
    ar = largura * altura
    print(f'O seu terreno tem {ar:.1f} m²')


def frescura():
    print('~=' * 20)

#PROGRAMA PRINCIPAL
frescura()

l = float(input('Qual a largura do seu terreno em metros: '))
al = float(input('Qual o comprimento: '))
area(l, al)
