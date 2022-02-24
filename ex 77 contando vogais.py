palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR')
for i in palavras:
    print(f'\nA palavra {i} tem as vogais: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
