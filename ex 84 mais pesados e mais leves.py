dados = list()
banco_de_dados = list()
mai = men = 0
maiores = list()
menores = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(str(input('Peso: ')))
    if len(banco_de_dados) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]
    banco_de_dados.append(dados[:])
    dados.clear()
    terminar = ' '
    while terminar != 'N' and terminar != 'S':
        terminar = str(input('Quer cadastrar mais uma pessoa? [S/N]: ')).upper().strip()
    if terminar == 'N':
        break
for c in banco_de_dados:
    if c[1] == mai:
        maiores.append(c[0])
    if c[1] == men:
        menores.append(c[0])
print(f'Foram cadastradas {len(banco_de_dados)} pessoas')
print(f'As pessoas mais pesadas "{mai}Kg" são', end=' ')
for c in maiores:
    print(f'[{c}]', end='')

print(f'\nAs pessoas mais leves "{men}Kg" são', end=' ')
for c in menores:
    print(f'[{c}]', end=' ')
