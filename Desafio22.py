print('====== DESAFIO 22 ======')
n = input('Digite seu nome completo: ')
print('Seu nome em letra maíscula: {}'.format(n.upper()))
print('Seu nome em letra minuscula: {}'.format(n.lower()))
lista = n.split()
print('Seu nome contém {} letras ao todo e seu primeiro nome é {} que contém {} letras.'.format(len(''.join(lista)), lista[0], len(lista[0])))