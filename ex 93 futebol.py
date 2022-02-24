fut = dict()
gols = list()
fut['jogador'] = str(input('NOME DO JOGADOR: '))
n = int(input('partidas jogadas: '))
for c in range(0, n):
    gols.append(int(input(f'quantos gols {fut["jogador"]} marcou na partida {c+1}: ')))
fut['gols'] = gols
fut['total'] = sum(gols)
print('-='*25)
print(fut)
print('-='*25)
for k, v in fut.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*25)
print(f'O jogador {fut["jogador"]} jogou {n} partidas')
for m, n in enumerate(gols):
    print(f'    => na partida {m+1} marcou {n} gols')
print(f'foi um total de {fut["total"]} gols')
