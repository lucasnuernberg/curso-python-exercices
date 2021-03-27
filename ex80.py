lista = []
for n in range(0, 5):
    v = int(input('Digite um número: '))
    if n == 0 or v > max(lista):
        lista.append(v)
        print(f'O número {v} foi adicionado na primeira posição')
    elif v < min(lista):
        lista.insert(0, v)
        print(f'O número {v} foi adicionado na posição 1')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]: #quando número é inserido o laço é cortado
                lista.insert(pos, v)
                print(f'O número {v} foi adiconado na posição {pos + 1}')
                break
            pos += 1 #soma pos até o número se encaixar
print('-='*20)
print(lista)



