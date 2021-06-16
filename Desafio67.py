print('====== DESAFIO 67 ======')
total = 0
while True:
    n = int(input('\nDigite o número para mostrar sua tabuada [-1 para parar]: '))
    if n < 0:
        break
    for c in range (1, 11):
        total = n * c
        print('{} x {} = {}'.format(n, c, total))
print('\nPrograma tabuada finalizado! Volte sempre!')