fut = dict()
dados = list()
gols = list()
controle = ' '
# COLHIMENTO DE DADOS / CADASTRO DOS JOGADORES
while True:
    fut['jogador'] = str(input('Nome do jogador: '))
    tot = int(input(f'quantas partidas {fut["jogador"]} jogou?: '))
    for c in range(0, tot):
        gols.append(int(input(f'quantos gols {fut["jogador"]} marcou na partida {c+1}: ')))
    fut['gols'] = gols[:]
    fut['total'] = sum(gols)
    dados.append(fut.copy())
    gols.clear()
    while True:
        controle = str(input('Quer cadastrar mais algum jogador [S/N] ?: ')).upper().strip()
        if controle in 'SN':
            break
        print('Por favor, use apenas S ou N')
    if controle == 'N':
        break
print('=-'*20)
print('cod  ', end='')
for i in fut.keys():
    print(f'{i:<15}', end='')
print()
for c, d in enumerate(dados):
    print(c+1, end=' '*5)
    for v in d.values():
        print(f'{str(v):<15}', end='')
    print()
while True:
    jogador = int(input('Quer saber os dados de qual jogador? [0 para parar]: '))
    if jogador == 0:
        break
    if jogador > len(dados):
        jogador = int(input('Digite um jogador válido: '))
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {dados[jogador - 1]["jogador"]}')
        for m, n in enumerate(dados[jogador-1]['gols']):
            print(f'No jogo {m+1}, {dados[jogador - 1]["jogador"]} fez {n} gols')
print('OBRIGADO')
