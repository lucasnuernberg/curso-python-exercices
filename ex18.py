#lendo um ângulo
from math import sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))

seno = sin(angulo)
cos = cos(angulo)
tang = tan(angulo)

print(f'Esse angulo tem o seno = {seno:.2f}, cosseno = {cos:.2f} e a tangente = {tang:.2f}')