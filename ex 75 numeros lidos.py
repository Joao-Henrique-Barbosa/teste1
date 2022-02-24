prim = float(input('Digite um numero: '))
seg = float(input('Digite outro numero: '))
terc = float(input('Digite mais um numero: '))
quart = float(input('Digite um ultimo numero: '))
tupla = (prim, seg, terc, quart)
'''num = (int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')),
       int(input('digite um numero: ')))'''
nove = par = tres = 0
for c in tupla:
    if c == 9:
        nove += 1
        #tupla.count(9)
    if c % 2 == 0:
        par += 1
    if c == 3:
        tres = tupla.index(3) + 1
print(f'O numero "9" foi digitado {nove} vezes')
if tres > 0:
    print(f'A primeira vez que o numero "3" aparece é na posição {tres}')
elif tres == 0:
    print(f'O numero tres nao apareceu nenhuma vez')
print(f'Entre todos os valores apresentados, {par} são pares e eles são: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
