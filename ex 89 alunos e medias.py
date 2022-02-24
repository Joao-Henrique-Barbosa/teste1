geral = list()
aluno = list()
nota = list()
media = cont = notas = n1 = n2 = numnome = 0
aluno.append(str(input('Nome: ')))
nota.append(float(input('Nota 1: ')))
nota.append(float(input('Nota 2: ')))
aluno.append(nota[:])
geral.append(aluno[:])
aluno.clear()
nota.clear()
# info vai receber a lista "nome" com a lista "nota" inserida
# O nome é considerado um termo da lista geral, e as duas notas são uma lista, considerado como o segundo termo
for infos in geral:
    # geral[0] = infos
    n1 = geral[cont][1][0]
    n2 = geral[cont][1][1]
    media = (n2 + n1) / 2
    numnome = 20 - len(geral[cont][0])
    print(f'{cont} {geral[cont][0]} {media}')
    cont += 1
saber = str(input('Quer saber as duas notas de algum aluno? [S/N]: ')).upper().strip()
numaluno = int(input('Qual é o numero do aluno?: '))
print(f'As notas do(a) {geral[numaluno][0]} são {geral[numaluno][1][0]} e {geral[numaluno][1][1]}')
print(f'{" Programa de notas encerrado ":-^50}')
