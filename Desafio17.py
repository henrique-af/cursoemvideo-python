print('====== DESAFIO 17 ======')
import math
co = float(input('Digite o valor do cateto oposto do triângulo: '))
ca = float(input('Digite o valor do cateto adjacente do triângulo: '))
hip = math.hypot(co, ca)
print('O valor da hipotenusa desse triângulo é de {}'.format(hip))