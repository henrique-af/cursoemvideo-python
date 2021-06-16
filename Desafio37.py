from time import sleep
print('====== DESAFIO 37 ======')
n = int(input('Digite um número para conversão: '))
menu = int(input('Selecione a opção\n'
             '1 - Converter para binário\n'
             '2 - Converter para octal\n'
             '3 - Converter para hexadecimal\n'
             'Sua opção? '))
print('Convertendo.....')
sleep(0.5)
if menu == 1:
    print('O número em binário fica {}.'.format(str(bin(n))[2:]))
elif menu == 2:
    print('O número em octal fica {}.'.format(str(oct(n))[2:]))
elif menu == 3:
    print('O número em hexadecimal fica {}.'.format(str(hex(n))[2:]))
else:
    print('Opção inválida, encerrando o programa!')

