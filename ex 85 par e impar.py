fonte = list()
par = list()
impar = list()
fonte.append(par)
fonte.append(impar)
for c in range(1, 8):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Os numeros pares digitados foram: {fonte[0]}')
print(f'Os numeros impares digitados foram: {fonte[1]}')
