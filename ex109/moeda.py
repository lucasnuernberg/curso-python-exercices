def aumentar(m, t, formatado=False):
    taxa = t / 100 + 1
    resp = m * taxa
    return resp if formatado is False else moeda(resp)

def metade(m, cond=False):
    resp = m / 2
    if cond:
        resp = moeda(resp)
    return resp

def diminuir(m):
    resp = m * 0.87
    return resp

def dobro(m=0, form=False):
    resp = m * 2
    if form:
        resp = moeda(resp, 'R$')
    return resp

def moeda(v=0, moeda= 'R$'):
    resp = f'{moeda}{v:.2f}'.replace('.', ',')
    return resp

