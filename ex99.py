from time import sleep
print('')
def maior(*num):
    if len(num) == 0:
        print('Analizando os valores passados...')
        print(f'Foram informados {len(num)} valores')
    else:
        print('Analizando os valores passados...')
        for c in num:
            print(c, end=' ')
            sleep(0.3)
        print(f'Foram informados {len(num)} valores')
        print(f'O maior valor passado foi {max(num)}')
        print('='*30)


maior(3, 4, 5)
maior(1, 2, 3, 4, 5, 5)
maior(0, 3, 1, 90, -3, 100, 4)
maior()