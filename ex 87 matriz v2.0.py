num = list()
col3 = list()
linha2 = list()
cont = par = soma3 = 0
for c in range(1, 10):
    if c <= 3:
        num.append(int(input(f'Digite um numero para a posição [1,{c}]: ')))
    elif c <= 6:
        num.append(int(input(f'Digite um numero para a posição [2,{c-3}]: ')))
    elif c <= 9:
        num.append(int(input(f'Digite um numero para a posiçao [3,{c-6}]: ')))
for c in num:
    if c % 2 == 0:
        par += c
for c in range(2, 10, 3):
    soma3 += num[c]
linha2.append(num[3:6])
maior2 = linha2[0][0]
for c in linha2:
    for n in c:
        if maior2 < n:
            maior2 = n
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {maior2}')
