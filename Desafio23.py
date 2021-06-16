print('====== DESAFIO 23 ======')
n = int(input('Digite um número: '))

unidade = n//1%10
dezena = n//10%10
centena = n//100%10
milhar = n//1000%10

print('Unidade: {:.0f}'.format(unidade))
print('Dezena: {:.0f}'.format(dezena))
print('Centena: {:.0f}'.format(centena))
print('Milhar: {:.0f}'.format(milhar))
