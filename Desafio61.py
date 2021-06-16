print('====== DESAFIO 61 ======')
print('Gerador de PA')
print('~'*20)
print('Vão ser mostrados 10 termos!')
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
while c <= 10:
    print('{} > '.format(t), end='')
    t += r
    c += 1
print('Acabou-se.')
