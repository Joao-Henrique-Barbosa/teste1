from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print('Os numeros sorteados foram: {}'.format(num))
print(f'O maior numero sorteado foi {max(num)} ')
print(f'O menor numero sorteado foi {min(num)}')
'''while True:
    num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
    print('Os numeros sorteados foram: {}'.format(num))
    print(f'O maior numero sorteado foi {max(num)} ')
    print(f'O menor numero sorteado foi {min(num)}')
   primeiro = num[0]
    maior = primeiro
    menor= primeiro
    # ESTRUTURA DE REPETIÇÃO PARA A DEFINIÇÃO DO MENOR NUMERO
    if num[1] > maior:
        maior = num[1]

    if num[2] > maior:
        maior = num[2]

    if num[3] > maior:
        maior = num[3]

    if num[4] > maior:
        maior = num[4]
    # ESTRUTURA DE REPETIÇÃO PARA A DEFINIÇÃO DO MAIOR NUMERO
    if num[1] < menor:
        menor = num[1]

    if num[2] < menor:
        menor = num[2]

    if num[3] < menor:
        menor = num[3]

    if num[4] < menor:
        menor = num[4]
    print(f'O MAIOR NUMERO É {maior}')
    print(f'O MENOR NUMERO É {menor}')
    terminar = ' '
    while terminar != 'S' and terminar != 'N':
        terminar = str(input('Quer sortear outros numero? [S/N]: ')).upper().strip()
    if terminar == 'N':
        break'''
print('Obrigado por usar nosso programa')