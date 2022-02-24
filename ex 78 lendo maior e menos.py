numeros = list()
print('=-'*50)
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número correspondente a posição {c}: ')))
    if c == 0:
        maior = menor = numeros[0]
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f'Os valores digitados foram {numeros}')
print(f'O maior valor digitado foi: {maior} na(s) posição(ões): ', end='')
for pos, v in enumerate(numeros):
    if v == maior:
        print(pos, end='... ')
print(f'\nO menor valor digitado foi: {menor} na(s) posição(ões): ', end='')
for pos, v in enumerate(numeros):
    if v == menor:
        print(pos, end='... ')
