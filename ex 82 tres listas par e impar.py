todos = list()
par = list()
impar = list()
while True:
    num = int(input('Digite um numero: '))
    todos.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    parada = ' '
    while parada != 'S' and parada != 'N':
        parada = str(input('Deseja continuar digitando numeros? [S/N]: ')).upper().strip()
    if parada == 'N':
        break
print(f'Os numeros digitados foram: {todos}\n'
      f'Os numeros pares digitados foram {par}\n'
      f'E os numeros impares digitados foram {impar}')