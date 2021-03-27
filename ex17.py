#calculando a hipotenuso

import math

co = int(input('Digite o cateto oposto do triângulo retângulo: '))
ca = int(input('Digite o cateto adjacente do triângulo retângulo: '))
hipotenusa = math.hypot(co, ca)
print(f'A hipotenusa desse triângulo é {hipotenusa:.2f}')