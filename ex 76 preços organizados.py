listagem = ('lapis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 25,
            'tranferidor', 4.20,
            'compasso', 9.90,
            'Mochila', 120.32,
            'canetas', 22.30,
            'livro', 34.90)
print('-'*40)
print(f'{"Lojas Joao Henrique": ^40}')
print('-'*40)
for pos in listagem:
    if type(pos) is str:
        print('{:.<30}'.format(pos), end='')
    if type(pos) is float or type(pos) is int:
        print('R$ {: >7.2f}'.format(pos))
print('-'*40)
