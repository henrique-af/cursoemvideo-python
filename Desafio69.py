print('====== DESAFIO 69 ======')
maior18 = homem = mulher = 0
while True:
    print('~ ~ Cadastre a pessoa ~ ~')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('~ '*5)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if continuar != 'SN':
            print('Digite S ou N, por favor.')
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if idade < 20 and sexo == 'F':
        mulher += 1
    if continuar == 'N':
        break
print(f'Total de pessoas maiores de 18: {maior18}')
print(f'Ao todo temos {homem} homem(s) cadastrado(s).')
print(f'E temos {mulher} mulher(es) com menos de 20 anos.')
