print('====== DESAFIO 35 ======')
print('__ANALISADOR DE TRIÂNGULOS__')
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))


if a < (b+c) and b < (a+c) and c < (a+b):
    print('\033[1:32:40mEsse triângulo é válido.\033[m')
else:
    print('\033[1:31:47mEEsse triângulo não é válido.\033[m')