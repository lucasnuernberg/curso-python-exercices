#FUNÇÕES EIA
def fatorial(num, show=False):
    """
    --> calcula fatorial
    :param num: número que se calcula o fatorial
    :param show: da a opção de mostrar o cálculo
    :return: retorna o valor de fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f = f*c
        if show and c > 0:
            print(c, end= ' ')
            if c > 1:
                print('x', end=' ')
            if c == 1:
                print('=', end=' ')
    return f

#aprendando boas praticas
help(fatorial)

