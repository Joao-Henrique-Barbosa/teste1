from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Data de nascimento: '))
dados['ctps'] = int(input('CTPS: '))
if dados['ctps'] == 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('salario: '))
    dados['aposentadoria'] = 35 - (date.today().year - dados['contratação']) + dados['idade']
for k, v in dados.items():
    print(f'{k} tem valor {v}')
