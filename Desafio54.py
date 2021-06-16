print('====== DESAFIO 54 ======')
from datetime import date
ano = date.today().year
jovem = 0
velho = 0
for c in range(1, 8):
    n = int(input('Em que ano a {}ª nasceu? '.format(c)))
    if (ano - n) >= 21:
        velho += 1
    else:
        jovem +=1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(velho))
print('E também tivemos {} pessoas menores de idade.'.format(jovem))

