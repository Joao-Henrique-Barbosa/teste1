todos = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um numero: '))
    todos.append(num)
    parada = ' '
    while parada != 'S' and parada != 'N':
        parada = str(input('Deseja continuar digitando numeros? [S/N]: ')).upper().strip()
    if parada == 'N':
        break
for c in todos:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Os numeros digitados foram: {todos}\n'
      f'Os numeros pares são: {par}\n'
      f'Os numeros impares são {impar}')
