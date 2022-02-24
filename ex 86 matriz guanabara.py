matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = list()
col3 = mai2 = somapar = 0
for l in range(1, 4):
    for i in range(1, 4):
        matriz[l-1][i-1] = int(input(f'Digite um numero para a posição [{l}, {i}]: '))
print('=-' * 45)
for l in range(1, 4):
    for i in range(1, 4):
        print(f'[{matriz[l-1][i-1]: ^5}]', end=' ')
        if matriz[l-1][i-1] % 2 == 0:
            par.append(matriz[l-1][i-1])
        if l == 2:
            if i == 1:
                mai2 = matriz[l-1][i-1]
            elif i > 1:
                if matriz[l-1][i-1] > mai2:
                    mai2 = matriz[l-1][i-1]
        if i == 3:
            col3 += matriz[l-1][i-1]
    print()
for c in par:
    somapar += c
print(f'A soma dos numeros pares da matriz é: {somapar}')
print(f'A soma dos valores da terceira coluna é: {col3}')
print(f'O maior numero da segunda linha é: {mai2}')
