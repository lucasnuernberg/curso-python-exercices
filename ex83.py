#ultimo da aula 17
ex = str(input('Digite uma expressão: '))
lista = []
for sim in ex:
    if sim == '(':
        lista.append(sim)
    elif sim == ')':
        if len(lista) > 0:
            lista.pop()
            break

if len(lista) == 0:
    print('Expressão esta correta')
else:
    print('Incorreto, reveja sua a expressão')
