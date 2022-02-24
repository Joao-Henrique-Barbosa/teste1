boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['nota'] = float(input('Nota: '))
if boletim['nota'] >= 7:
    boletim['situação'] = 'aprovado'
elif 5 <= boletim['nota'] < 7:
    boletim['situação'] = 'recuperação'
else:
    boletim['situação'] = 'reprovado'
print('=-'*30)
for k, v in boletim.items():
    print(f'{k} é {v}')
