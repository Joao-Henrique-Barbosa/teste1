num = list()
while True:
    leitor = int(input('Digite um numero: '))
    if leitor not in num:
        num.append(leitor)
        print('Valor unico! Adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar')
    parada = ' '
    while parada != 'S' and parada != 'N':
        parada = str(input('Quer continuar [S/N]: ')).upper().strip()
    if parada == 'N':
        break
num.sort()
print(f'Os valores computados foram: {num}')
