print ('====== DESAFIO 04 ======')
n = input('Digite algo: ')
print('O tipo desse algo é: ', type(n))
print('É um número? {} | É uma letra? {} | É alfanúmerico? {} | Somente espaços? {} | Está em maiúsculas? {} | Está em minúsculas? {} | Está capitalizada? {}' .format(n.isnumeric(), n.isalpha(), n.isalnum(), n.isspace(), n.isupper(), n.islower(), n.istitle()))