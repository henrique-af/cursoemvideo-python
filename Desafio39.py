print('====== DESAFIO 39 ======')
from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano

if idade == 18:
    print('Você vai se alistar esse ano!\n'
          'Corre para se alistar!')
elif idade > 18:
    print('Quem nasceu em {} tem {} em {}.\n'
          'Você devia ter se alistado a {} atrás.\n'
          'Seu alistamento foi em {}.'.format(ano, idade, atual, (idade - 18), (ano + 18)))
else:
    print('Quem nasceu em {} tem {} em {}.\n'
          'Ainda faltam {} anos para se alistar.\n'
          'Seu alistamento será em {}.'.format(ano, idade, atual, (18 - idade), (ano + 18)))



