print('====== DESAFIO 70 ======')
print('~ '*8)
print('Acervo barato :p')
print('~ '*8)
total = produtomaiorque1000 = preçobarato = cont = 0
nomebarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('R$ '))
    total += preço
    cont += 1
    armazenavalor = preço
    continuar = ' '
    if preço > 1000:
        produtomaiorque1000 += 1
    if cont == 1 or preço < preçobarato:
        preçobarato = preço
        nomebarato = produto
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtomaiorque1000} produto(s) custando mais que R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${preçobarato:.2f}')
