# verificando se é um número
def leiaint(n):
    num = input(n)
    while not num.isnumeric():
        print('\033[31mERRO!\033[m')
        num = input(n)
    return num

v = leiaint('Digite um numero: ')
print(f'O número {v} foi digitado')