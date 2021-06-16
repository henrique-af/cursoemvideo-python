print('====== DESAFIO 41 ======')
from datetime import date
atual = date.today().year
n = int(input('Ano de nascimento: '))
idade = atual - n

if idade < 9:
    print('O atleta tem {} anos.\n'
          'CLASSIFICAÇÃO: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos.\n'
          'CLASSIFICAÇÃO: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos.\n'
          'CLASSIFICAÇÃO: JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos.\n'
          'CLASSIFICAÇÃO: SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos.\n'
          'CLASSIFICAÇÃO: MASTER'.format(idade))