print('====== DESAFIO 59 ======')
print('~~~ CALCULADORA ~~~')
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
print('1 - Somar\n'
      '2 - Multiplicar\n'
      '3 - Maior\n'
      '4 - Novos números\n'
      '5 - Sair do programa')
menu = int(input('Qual sua opção? '))
while menu != 5:
    if menu not in (1, 2, 3, 4, 5):
        menu = int(input('Opção errada, digite novamente: '))
    else:
        if menu == 1:
            print('Opção soma escolhida!\n')
            print('A soma dos valores é igual a {}.\n'.format((n1 + n2)))

            print('1 - Somar\n'
                  '2 - Multiplicar\n'
                  '3 - Maior\n'
                  '4 - Novos números\n'
                  '5 - Sair do programa')
            menu = int(input('Digite uma nova opção: '))
        elif menu == 2:
            print('Opção multiplicação escolhida!')
            print('A multiplicação dos valores é igual a {}\n'.format((n1 * n2)))

            print('1 - Somar\n'
                  '2 - Multiplicar\n'
                  '3 - Maior\n'
                  '4 - Novos números\n'
                  '5 - Sair do programa')
            menu = int(input('Digite uma nova opção: '))
        elif menu == 3:
            print('Opção de comparação escolhida!')
            if n1 > n2:
                print('O número {} é maior que {}\n'.format(n1, n2))
                print('1 - Somar\n'
                      '2 - Multiplicar\n'
                      '3 - Maior\n'
                      '4 - Novos números\n'
                      '5 - Sair do programa')
                menu = int(input('Digite uma nova opção: '))
            else:
                print('O número {} é maior que {}\n'.format(n2, n1))
                print('1 - Somar\n'
                      '2 - Multiplicar\n'
                      '3 - Maior\n'
                      '4 - Novos números\n'
                      '5 - Sair do programa')
                menu = int(input('Digite uma nova opção: '))
        elif menu == 4:
            n1 = float(input('Digite o 1º número: '))
            n2 = float(input('Digite o 2º número: '))
            print('\n1 - Somar\n'
                  '2 - Multiplicar\n'
                  '3 - Maior\n'
                  '4 - Novos números\n'
                  '5 - Sair do programa')
            menu = int(input('Digite uma nova opção: '))
print('Programa finalizado!')
