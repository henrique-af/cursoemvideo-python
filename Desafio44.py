print('====== DESAFIO 44 ======')
produto = float(input('Valor do produto: R$'))
menu = int(input('Selecione o metódo de pagamento\n'
                 '1 - À vista (dinheiro ou cheque) - 10% de desconto\n'
                 '2 - À vista (cartão) - 5% de desconto\n'
                 '3 - Parcelamento em 2x (cartão) - Sem desconto\n'
                 '4 - Parcelamento em 3x ou mais (cartão) - 20% de juros\n'
                 'Qual a opção? '))

if menu == 1:
    print('A vista, o valor do produto fica R${:.2f}'.format(produto * 0.90))
elif menu == 2:
    print('A vista no cartão, o valor do produto fica R${:.2f}'.format(produto * 0.95))
elif menu == 3:
    print('Parcelando em 2x, o valor da parcela fica R${:.2f}'.format(produto / 2))
elif menu == 4:
    parcela = int(input('Parcelando com juros, quantas vezes deseja parcelas? '))
    print('\nCom parcelamento em {}x, o valor da parcela fica R${:.2f}\n'
          'E o valor total fica R${:.2f}'.format(parcela, ((produto * 1.20)/parcela),(produto * 1.20)))
else:
    print('Opção inválida, finalizando o programa!')