print('====== DESAFIO 53 ======')
n = str(input('Digite uma frase: ')).upper().replace(' ', '')
n1 = n[::-1]
print('O inverso de {} é {}.'.format(n, n1))
if n == n1:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo.')