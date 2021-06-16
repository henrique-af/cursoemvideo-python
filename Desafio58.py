print('====== DESAFIO 58 ======')
from secrets import randbelow
from time import sleep
print('Computador falando...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')
cont = 0
computador = randbelow(11)
jogador = int(input('Qual é o seu palpite? '))
sleep(0.5)
if jogador == computador:
    cont += 1
    sleep(0.5)
    print('Acertou com {} tentativas. Parabéns!'.format(cont))
else:
    while jogador != computador:
        if computador > jogador:
            sleep(0.5)
            print('Mais... Tente mais uma vez.')
            jogador = int(input('Qual é o seu palpite? '))
            cont +=1
        else:
            sleep(0.5)
            print('Menos... Tente mais uma vez.')
            jogador = int(input('Qual é o seu palpite? '))
            cont +=1
    sleep(0.5)
    print('Acertou com {} tentativas. Parabéns!'.format(cont))