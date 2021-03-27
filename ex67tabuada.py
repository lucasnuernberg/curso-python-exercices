vezes = 0
while True:
    cont = 1
    print('\033[31m=\033[m'*34)
    num = int(input('Qual a tabuada que você quer ver:(-1 PARA SAIR)'))
    print('\033[31m=\033[m' * 34)
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} X {cont} = {num * cont}')
        cont += 1
    vezes += 1
print('\033[31m=\033[m'*34)
print(f'Você viu {vezes} tabuadas')
print('Volte sempre')
