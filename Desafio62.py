print('====== DESAFIO 62 ======')
print('Gerador de PA')
print('~'*20)
print('Vão ser mostrados 10 termos!')
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while c <= tot:
        print('{} > '.format(t), end='')
        t += r
        c += 1
    print('Pausa')
    m = int(input('Quantos termos você quer a mais? '))
print('Acabou-se.')
print('Foram mostrados {} termos.'.format(c-1))