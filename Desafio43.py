print('====== DESAFIO 43 ======')
peso = float(input('Digite seu peso atual (kg): '))
altura = float(input('Digite a sua altura (m): '))

if peso == 0 or altura == 0:
    print('Valores inválidos, execute novamente a calculadora!')
else:
    if peso / (altura ** 2) <= 18.5:
        print('\nVocê está abaixo do peso.')
    elif peso / (altura ** 2) <= 25:
        print('\nPeso ideal, parabéns!')
    elif peso / (altura ** 2) <=30:
        print('\nVocê está com sobrepeso.')
    elif peso / (altura ** 2) <=40:
       print('\nVocê está com grau de obesidade.')
    else:
        print('\nVocê está no grau de obesidade morbida.')
    print('O IMC é de {:.1f}'.format(peso / (altura ** 2)))