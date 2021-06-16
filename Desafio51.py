print('====== DESAFIO 51 ======')
print('~'*20)
print('10 Termos de uma PA')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = n + (10 - 1) * r
for c in range(n, d, r):
    print('{} ~ '.format(c), end='')
print('Fim!')
