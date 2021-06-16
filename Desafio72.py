print('====== DESAFIO 72 ======')
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
c = int(input('Qual número deseja mostrar por extenso? [0 a 20]: '))
while True:
    if c not in range(21):
        c = int(input('Tente novamente. Qual número deseja mostrar por extenso? [0 a 20]: '))
    else:
        break
print(f'Você digitou {tupla[c]}.')