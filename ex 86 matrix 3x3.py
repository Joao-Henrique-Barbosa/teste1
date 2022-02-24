num = list()
cont = 0
for c in range(1, 10):
    if c <= 3:
        num.append(int(input(f'Digite um numero para a posição [1,{c}]: ')))
    elif c <= 6:
        num.append(int(input(f'Digite um numero para a posição [2,{c-3}]: ')))
    elif c <= 9:
        num.append(int(input(f'Digite um numero para a posiçao [3,{c-6}]: ')))
for c in num:
    cont += 1
    if cont != 3 and cont != 6:
        print(f'[{c: ^5}]', end='')
    else:
        print(f'[{c: ^5}]')
