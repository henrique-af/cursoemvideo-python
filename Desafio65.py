print('====== DESAFIO 65 ======')
tot = menor = maior = cont = 0
s = 'S'
while s in 'Ss':
    n = int(input('Digite um número: '))
    s = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    tot = tot + n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média foi {}.\n'
'O maior valor foi {} e o menor {}.'.format(cont, (tot / cont), maior, menor))