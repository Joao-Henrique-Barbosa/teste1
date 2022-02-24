from random import randint
lista = list()
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')


    if num < lista[0]:
        lista.insert(0, num)
        print('Adicionando no começo da lista')


    if c == 2:
        if num <= lista[-1] and num <= lista[0]:
            lista.insert(1, num)
            print('Adicionando na posição 1 da lista')
    if c == 3:
        if num >= lista[0] and num <= lista[1]:
            lista.insert(1, num)
            print('Adicionando na posição 1 da lista')
        elif num >= lista[1] and num <= lista[-1]:
            lista.insert(2, num)
    if c == 4:
        if num >= lista[0] and num <= lista[1]:
            lista.insert(1, num)
            print('Adicionando na posição 1 da lista')
        elif num >= lista[1] and num <= lista[2]:
            lista.insert(2, num)
            print('Adicionando na posição 2 da lista')
        elif num >= lista[2] and num <= lista[-1]:
            lista.insert(3, num)
            print('Adicionando na posição 3 da lista')
print(lista)
