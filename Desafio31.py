print('====== DESAFIO 31 ======')
d = float(input('Digite a distância da viagem em Km: '))
if d > 200:
    preco = d * 0.45
    print('O preço da passagem será de R${:.2f}'.format(preco))
else:
    preco = d * 0.50
    print('O preço da viagem será de R${:.2f}'.format(preco))