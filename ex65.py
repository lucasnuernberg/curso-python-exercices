#sim ou não

resp = 'S'
maior = soma = cont = menor =  0
while resp in 'S':
    num = int(input('\nDigite um número: '))
    resp = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    cont += 1
    soma += num
    if cont == 1:#no primeiro valor inserido o maior e menor são iguais
        menor = maior = num
    elif num < menor:
            menor = num
    elif num > maior:
        maior = num
media = soma/cont
print('='*30)
print('A média dos {} números digitados é {:.2f}'.format(cont, media))
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))