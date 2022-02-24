lista = list()
login = dict()
media = 0
while True:
    login['nome'] = str(input('nome: '))
    while True:
        login['sexo'] = str(input('sexo [M/F]: ')).upper().strip()
        if login['sexo'] in 'MF':
            break
        print('ERROR TENTE APENAS M OU F')
    login['idade'] = int(input('idade: '))
    media += login['idade']
    lista.append(login.copy())
    while True:
        resp = str(input('quer continuar? [S/N}: ')).upper().strip()
        if resp == 'SN':
            break
        print('USE APENAS S OU N')
    if resp == 'N':
        break
print(f'A) ao todo, {len(lista)} pessoas foram cadastradas')
print(f'B) a média de idade é igual a {media/len(lista)}')
print(f'C) as mulheres cadastradas foram: ', end='')
for c in range(0, len(lista)):
    if lista[0]['sexo'] == 'F':
        print(lista[c]["nome"], end=' ')
print()
print('D) lista de pessoas com idade acima da média: ')
for d in lista:
    if login['idade'] >= media/len(lista):
        for k, v in d.items():
            print(f'{k} = {v}; ', end='')
        print()
''''for c in range(0, len(lista)):
    if lista[c]['idade'] > media/len(lista):
       print(f'nome = {lista[c]["nome"]}; sexo = {lista[c]["sexo"]}; idade = {lista[c]["idade"]}')'''''