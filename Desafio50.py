print('====== DESAFIO 50 ======')
soma = 0
p = 0
for c in range (1, 7):
    v = int(input('Digite o {} valor: '.format(c)))
    if (v % 2 == 0):
        soma += v
        p += 1
print('A soma total é {}, foram informados {} pares.'.format(soma, p))
