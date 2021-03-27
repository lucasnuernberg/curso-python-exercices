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
    print('-'*27)
    print(f'{"RESUMO":^25}')
    print('-' * 27)
    print(f'{"Preço analizado:":>5}{moeda(v):>10}')
    print(f'{"Dobro do preço:":>5} {dobro(v, True):>10}')
    print(f'{"Metade do preço:":>5}{metade(v, True):>9}')
    print(f'{f"{a}% de aumento:":>5} {moeda((aumentar(v, a))):>10}')
    print(f'{f"{d}% de redução:":>5}{moeda(diminuir(v, d)):>10}')
    print('-' * 27)