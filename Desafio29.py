print('====== DESAFIO 29 ======')
v = float(input('Digite a velocidade do veicúlo em Km/h: '))
if v >= 80:
    limite = v - 80
    multa = limite * 7
    print('Por ultrapassar a velocidade, você foi multado em R${:.2f}'.format(multa))
else:
    print('Você estava dentro da velocidade limite.')