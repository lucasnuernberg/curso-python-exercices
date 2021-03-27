#sequência fibonacci 0, 1, 1, 2, 3, 5, 8, 13
print('{}=~'.format('\033[33m') * 10)
print('sequência fibonacci'.capitalize())
print('=~' * 10)
vezes = int(input('Quantos números da sequência você quer: '))
t1 = 0
t2 = 1
while vezes > 0:
    print(t1, '--->', end='')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    vezes = vezes - 1
print(' FIM')
