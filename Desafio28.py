print('====== DESAFIO 28 ======')
from secrets import randbelow
from time import sleep
n = int(input('Adivinhe o número de 0 a 5: '))
cn = randbelow(6)
print('Escolhendo.........')
sleep(3)
if n == cn:
    print('Parábens, você acertou!')
else:
    print('Que pena, errou! Meu número é o {}.'.format(cn))
