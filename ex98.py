from time import sleep
def contador(ini, final, passo):
    print('\033[31m=\033[m'*30)
    if passo == 0:
        passo = 1
    if passo < 0:
        add = -1
        passo *= -1
    print(f'Contagem de {ini} até {final} de {passo} em {passo}')
    add = 1

    if ini > final and passo > 0:
        passo *= -1
        add = -1

    for p in range(ini, final + add, passo):
        print(p, end=' ')
        sleep(0.3)
    print('FIM!!!')



print('AGORA É TUA VEZ DE PERSONALIZAR')
print('\033[31m=\033[m'*30)
co = int(input('Inicio: '))
fi = int(input('Final: '))
pa = int(input('Passo: '))
contador(co, fi, pa)
