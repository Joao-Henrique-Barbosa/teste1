import random, time
terminar = ' '
dif = cont = 0
palpites = list()
todos = list()
print('\033[31m='*37)
print(f'{"NUMEROS DA MEGA SENA": ^37}')
print('='*37)
while True:
    jogos = int(input('\033[mQuantos jogos você quer que eu crie?: '))
    print(f'\033[31m{f" SORTEANDO {jogos} JOGOS ":=^37}\033[m')
    time.sleep(2)
    for c in range(1, jogos+1):
        while dif < 6:
            aleatorio = random.randint(1, 60)
            if aleatorio not in palpites:
                palpites.append(aleatorio)
                dif = dif + 1
        palpites.sort()
        todos.append(palpites[:])
        palpites.clear()
        dif = 0
    print(f'{"OS JOGOS SORTEADOS FORAM:": ^37}')
    for c in todos:
        time.sleep(1.5)
        cont += 1
        print(f'Jogo {cont}: {c}')
    while terminar != 'N' and terminar != 'S':
        terminar = str(input('Quer sortear mais jogos? [S/N]: ')).upper().strip()
        jogos = 0
    if terminar == 'S':
        cont = 0
    if terminar == 'N':
        break
print(f'\033[31m{"BOA SORTE":=^37}')
