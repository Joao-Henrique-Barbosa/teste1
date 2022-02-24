teams = ('Atlético - MG', 'Flamengo', 'Internacional', 'São Paulo', 'Fluminense', 'Santos', 'Palmeiras', 'Fortaleza',
         'Sport', 'Vasco', 'Ceará', 'Atlético - GO', 'Botafogo', 'Grêmio', 'Athletico - PR', 'Bahia', 'Corinthians',
         'Coritiba', 'Bragantino', 'Goiás')
while True:
    print(f'Todos os timer do brasileirão são: {teams}')
    print(f'Os 5 primeiros times são: {teams[:5]}')
#   print(f'Os 4 ultimos colocados são: {teams[-4:]}')
    print(f'Os 4 ultimos colocados são: {teams[16:]}')
    print(f'E a classificação em ordem alfabética é: {sorted(teams)}')
    print(f'O fluminense está na {teams.index("Fluminense") + 1}° posição')
    terminar = ' '
    while terminar != 'N' and terminar != 'S':
        terminar = str(input('Quer que eu mostr novamente? [S/N]: ')).strip().upper()
    if terminar == 'N':
        break
print('\033[31mObrigado por usar nosso programa')