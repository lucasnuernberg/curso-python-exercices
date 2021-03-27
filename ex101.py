from _datetime import date
ano = date.today().year
def eleicao(nasc):
    age = ano - nasc
    if age >= 65 or 18 > age >= 16:
        estado = 'VOTO OPCIONAL'
    elif age >= 18:
        estado = 'VOTO OBRIGATÓRIO'
    else:
        estado = 'NÃO VOTA'
    return estado
    return age



nasc = int(input('Em que ano você nasceu: '))
age = ano - nasc
print(f'{age}: {eleicao(nasc)}')

