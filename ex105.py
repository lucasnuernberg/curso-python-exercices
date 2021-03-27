def notas(*n, sit=False):
    """
    ----> boletim
    :param n: notas que o aluno recebeu
    :param sit: opção para ver a situação
    :return: retorna um dionario
    """
    dici = dict()
    quant = len(n)
    dici['total'] = quant
    dici['maior'] = max(n)
    dici['menor'] = min(n)
    dici['média'] = sum(n)/quant
    if sit:
        if dici['média'] >= 7:
            m = 'Boa'
        if dici['média'] < 7:
            m = 'Razoavel'
        if dici['média'] < 5:
            m = 'Ruim'
        dici['situação'] = m
    return dici


#programa principal
print('')
resp = notas(0, 4, 8, 5.9, True)
print(resp)
#help(notas)