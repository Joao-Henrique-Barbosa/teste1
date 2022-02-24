extenso = ('UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE',
           'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    numero = int(input('Escolha um numero de 0 a 20 para saber como ele é escrito por extenso: '))
    while numero > 20 or numero < 0:
        numero = int(input('Escolha um numero de 0 a 20 para saber como ele é escrito por extenso: '))
    print(f'O numemero {numero}, por extenso é: \033[31m{extenso[numero - 1]}\033[m')
    continuar = ' '
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Quer saber outro numero? [S/N}: ')).upper().strip()
    if continuar == 'N':
        break
print('OBRIGADO POR USAR MEU PROGRAMA, TENHA UM BOM DIA')