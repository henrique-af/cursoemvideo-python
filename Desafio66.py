print('====== DESAFIO 66 ======')
cont = s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print('A soma foi {} e foram digitados {} números.'.format(s, cont))