import random, time, operator
ranking = list()
jogadas = dict()
for c in range(1, 5):
    jogadas[f'jogador {c}'] = random.randint(1, 6)
for m, n in jogadas.items():
    print(f'O {m} tirou: {n}')
    time.sleep(1.5)
ranking = sorted(jogadas.items(), key=operator.itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'o {k+1} lugar é {v[0]} que tirou {v[1]}')
