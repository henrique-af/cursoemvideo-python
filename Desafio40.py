print('====== DESAFIO 39 ======')
from time import sleep
n1 = float(input('Digite a sua nota da N1: '))
n2 = float(input('Digite a sua nota da N2: '))
print('\nCalculando.............\n')
sleep(0.7)
if ((n1 + n2)/2) >= 7:
    print('Média maior que 7, APROVADO!')
elif ((n1+n2)/2) >=5 and ((n1+n2)/2) <= 6.9:
    print('Média insuficiente para passar direto, RECUPERAÇÃO!')
else:
    print('Média menor que 5, REPROVADO!')