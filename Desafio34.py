print('====== DESAFIO 33 ======')
n = float(input('Digite o salário do funcionário: R$'))
if n >= 1250:
    aumento = n * 1.10
else:
    aumento = n * 1.15
print('O salário com aumento ficou R${:.2f}'.format(aumento))