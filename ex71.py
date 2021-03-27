#verificando quantas cédulas de 50 serão necessárias
from time import sleep
valor = int(input('\nDigite o valor a ser sacado: '))
total = valor
cedula = 50 #começa valendo 50
totalced = 0

while True:
    if total >= cedula: #se o total de dinheiro for igual ou maior que a cedula ele executa
        total -= cedula #retira do total o valor da ceduça
        totalced += 1   #conta a cedula retirada
    else:
        if totalced > 0: #so aparece se tiver mais de 1 cedula
            print(f'O total de cedulas de {cedula} é {totalced}')
            sleep(1)
        if cedula == 50: #troca cedula quando não puder mais retirar do total
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0 #apos a troca de cedula ele zera para contar a proxima
        if total == 0:
            break

'''notas50 = valor // 50
notas20 = (valor - notas50*50)//20
notas10 = (valor - ((notas50*50)+(notas20*20)))//10
notas1 = (valor - ((notas50*50)+(notas20*20)+(notas10*10)))'''