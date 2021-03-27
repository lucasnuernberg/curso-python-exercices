from ex115.cabeca import *
from ex115.funcoes import *
criararq('cadastro.txt')
while True:
    choice = cab(['Ver cadastros', 'Adicionar pessoa', 'Fechar programa'])

    if choice == 1:
        #ver cadastros
        lerarq('cadastro.txt')

    elif choice == 2:
        alinhar('ADICIONAR PESSSOAS')
        nome = str(input('Nome: ').title())
        idade = leiaidade()
        adicionar('cadastro.txt', nome, idade)
    elif choice == 3:
        break
    else:
        print(f'{cores["vermelho"]}Digite um valor valido{cores["zera"]}')


print(f'{cores["verde"]}Volte Sempre')






