print('====== DESAFIO 42 ======')
from time import sleep
print('__ANALISADOR DE TRIÂNGULOS v2__')
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))


if a < (b+c) and b < (a+c) and c < (a+b):
    print('\nCalculando....\n')
    sleep(1)
    if a == b == c:
        print('\033[1:32:40mEsse triângulo é válido, formando um triângulo equilátero.\033[m')
    elif a != b != c != a:
        print('\033[1:32:40mEsse triângulo é válido, formando um triângulo escaleno.\033[m')
    else:
        print('\033[1:32:40mEsse triângulo é válido, formando um triângulo isósceles.\033[m')
else:
    print('\033[1:31:47mEsse triângulo não é válido.\033[m')