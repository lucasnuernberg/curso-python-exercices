import random
import time
lista = []
dados = []
contador = contador2 = 0
print(f'\n{"MEGA SENA DO QUILUNHAS":~^30}')
jogos = int(input('\nQuantos jogos você quer: '))
print(f'{f"SORTEANDO {jogos} JOGOS":=^30}')
while jogos > contador:
    contador2 = 0
    time.sleep(1)
    while contador2 < 6:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador2 += 1
    contador += 1
    dados.append(lista[:])
    lista.sort()
    print(f'Jogo {contador}: {lista}')
    lista.clear()
print(F'{"BOA SORTE":=^30}')

