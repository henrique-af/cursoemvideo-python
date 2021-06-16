print('====== DESAFIO 56 ======')
velho = 0
jovem = 0
cont = 0
totid = 0
fim = 0
for c in range (1, 5):
    print('~~~~ {}ª Pessoa ~~~~'.format(c))
    n = str(input('Nome: ')).strip()
    i = float(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    totid += i
    if s in 'Ff' and i < 20:
        cont += 1
    else:
        if i > 1:
            velho = i
            jovem = i
            nomev = n
            nomej = n
        if i > velho:
            velho = i
            nomev = n
        if i < jovem:
            jovem = i
            nomej = n
    if velho > jovem:
        fim = velho
        fim2 = nomev
    else:
        fim = jovem
        fim2 = nomej

print('A média de idade do grupo é de {} anos.'.format((totid / 4)))
print('O homem mais velho tem {.:1f} anos e se chama {}.'.format(fim, fim2))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))

