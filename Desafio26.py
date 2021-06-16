print('====== DESAFIO 26 ======')
frase = str(input('Digite a sua frase: ')).upper()

print('Na sua frase aparece {} vez(es) a letra A, primeira vez e a última aparecem respectivimente na {} posição.' .format(frase.count('A'), (frase.find('A'), (frase.rfind('A')))))