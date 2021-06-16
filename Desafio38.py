print('====== DESAFIO 38 ======')
print('-=-=- Comparação de valores -=-=-')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 == n2:
    print('Valores iguais!')
elif n1 > n2:
    print('O valor {:.1f} é maior que o valor {:.1f}'.format(n1, n2))
else:
    print('O valor {:.1f} é maior que o valor {:.1f}.'.format(n2, n1))
