from random import randint
lista = list()


def maior(num):
    print('=-'*25)
    print('Analisando os valores passsados...')
    for m, n in enumerate(num):
        print(n,  end=' ')
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


for c in range(0, 3):
    lista.clear()
    for g in range(0, 5):
        lista.append(randint(0, 9))
    maior(lista)
