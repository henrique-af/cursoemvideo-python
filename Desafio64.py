print('====== DESAFIO 64 ======')
c = 0
tot  = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    tot = tot + n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi de {}.'.format(c, tot))