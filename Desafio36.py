print('====== DESAFIO 36 ======')
print(':::::. SIMULADOR DE EMPRESTIMOS .:::::')
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário da pessoa: R$'))
anos = int(input('Quantos anos deseja parcelar: '))

parcela = casa / (anos * 12)

if parcela > salario * 0.30:
    print('\033[1:31:40mEmpréstimo não aprovado! Salário ou tempo de parcelamento incompátivel!\033[m')
else:
    print('\033[1:32:40mEmpréstimo aprovado! Parcela no valor de R${:.2f}\033[m'.format(parcela))

