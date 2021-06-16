print('====== DESAFIO 18 ======')
import math
a = float(input('Informe o valor do ângulo: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tgn = math.tan(math.radians(a))
print('O seno do ângulo corresponde a {:.1f}, cosseno a {:.1f} e a tangente a {:.1f}'.format(sen, cos, tgn))