print('====== DESAFIO 55 ======')
maior = 0
menor = 0
for c in range (1, 6):
    n = float(input('Peso da {}ª pessoa: '))
    if n == 1:
        menor = n
        maior = n
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg.'.format(maior))
print('O menor peso lido foi de {}kg.'.format(menor))

