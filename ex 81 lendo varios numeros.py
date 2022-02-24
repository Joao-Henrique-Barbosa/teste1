num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    parada = ' '
    while parada != 'S' and parada != 'N':
        parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if parada == 'N':
        break
num.sort(reverse=True)
print(f'Foram digitados {len(num)} numeros\nos numeros em ordem decrescente é: {num}')
if 5 in num:
    print(f'O numero 5 foi digitado')
else:
    print(f'O numero 5 nao foi digitado')
