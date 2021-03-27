# verificando se é um número
def leiaint():
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
        except(ValueError, TypeError):
            print('\033[31mErro, digite um número válido\033[m')
            continue
        else:
            return num

#
def leiafloat():
    while True:
        try:
            num = float(input('Digite um número Real: '))
        except (ValueError, TypeError):
            print('\033[31mErro, digite um número válido\033[m')
            continue
        else:
            return num




n1 = leiaint()
n2 = leiafloat()
print(f'-->Número inteiro: {n1}\n-->Número Real: {n2}')

