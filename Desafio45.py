print('====== DESAFIO 45 ======')
from time import sleep
import emoji
from random import randint
print(emoji.emojize('Suas opções:\n'
                 '1 - Pedra :fist:\n'
                 '2 - Papel :hand:\n'
                 '3 - Tesoura :v:\n', use_aliases=True))
menu = int(input('Qual a sua jogada? '))
computador = randint(1,3)
sleep(0.2)

if menu !=1 and menu !=2 and menu !=3:
    print('Opção inválida, finalizando o programa!')
else:
    print('\nJO')
    sleep(0.6)
    print('KEN')
    sleep(0.6)
    print('PO!')
    sleep(0.6)

    if menu == 1 and computador == 2:
        print(emoji.emojize('\nVocê perdeu! Computador escolheu papel :hand:',use_aliases=True))
    elif menu == 1 and computador == 3:
        print(emoji.emojize('\nVocê ganhou! Computador escolheu tesoura :v:',use_aliases=True))
    elif menu == 2 and computador == 3:
        print(emoji.emojize('\nVocê perdeu! Computador escolheu tesoura :v:',use_alises=True))
    elif menu == 2 and computador == 1:
        print(emoji.emojize('\nVocê ganhou! Computador escolheu pedra :fist:',use_aliases=True))
    elif menu == 3 and computador == 1:
        print(emoji.emojize('\nVocê perdeu! Computador escolheu pedra :fist:',use_aliases=True))
    elif menu == 3 and computador == 2:
        print(emoji.emojize('\nVocê ganhou! Computador escolheu papel :hand:',use_aliases=True))
    elif menu == computador:
        print('\nInfelizmente empatou!')