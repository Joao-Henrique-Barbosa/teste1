from random import randint
num = list()


def sorteia(lista):
    lista.clear()
    for c in range(0, 5):
        num.append(randint(0, 9))
    print(num)


def somaPar(lista):
    soma = 0
    for m, n in enumerate(lista):
        if n % 2 == 0:
            soma += n
    print(f'A soma dos numeros pares é {soma}')


sorteia(num)
somaPar(num)
