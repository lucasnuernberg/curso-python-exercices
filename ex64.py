cont = num = soma = 0

while num != 999:
    num = int(input('Digite [999] para parar: '))
    if num != 999:
        cont += num #somando os resultados
        soma += 1 #contando quantas vezes
print('\nA quantidade de números digitados foi {}\nA soma dessas dos números é {}'.format(soma, cont))