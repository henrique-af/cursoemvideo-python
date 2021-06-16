print('====== DESAFIO 32 ======')
from datetime import date
n = int(input('Digite um ano para saber se ele é bissexto: '))
if n == 0:
    n = date.today().year
if n%4== 0 and n%100 !=0 or n%400 ==0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')