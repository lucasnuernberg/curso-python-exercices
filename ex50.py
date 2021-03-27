soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('A soma dos {} valores pares digitados é {}'.format(cont, soma))
