def aumentar(m, t):
    taxa = t / 100 + 1
    resp = m * taxa
    return resp

def metade(m, cond=False):
    resp = m / 2
    if cond:
        resp = moeda(resp)
    return resp

def diminuir(m, t):
    resp = m * (1 - (t/100))
    return resp

def dobro(m=0, form=False):
    resp = m * 2
    if form:
        resp = moeda(m*2, 'R$')
    return resp

def moeda(v=0, moeda= 'R$'):
    resp = f'{moeda}{v:.2f}'.replace('.', ',')
    return resp

def resumo(v=0, a=0, d=0):
    if d <= 9:
        t = '\t'
    else:
        t = ''
    print('-'*27)
    print('RESUMO'.center(27))
    print('-' * 27)
    print(f'Preço analizado: \t{moeda(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'{"Metade do preço:"} \t{metade(v, True)}')
    print(f'{a}% de aumento: \t{moeda(aumentar(v, a))}')
    print(f'{d}% de redução: {t}\t{moeda(diminuir(v, d))}')
    print('-' * 27)