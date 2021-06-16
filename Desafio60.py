print('====== DESAFIO 60 ======')
n = int(input('Digite um número para\ncalcular seu fatorial: '))
c = 0
f = 1
for c in range (1, n):
    f *= n
    n -= 1
print ('Seu fatorial é {}.'.format(f))
