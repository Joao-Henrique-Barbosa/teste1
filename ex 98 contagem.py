import time, math


def contador(a, b, c):
    print('=-'*25)
    if c == 0:
        c = 1
    if a < b:
        print(f'contagem de {a} até {b} de {c} em {c}')
        for m in range(a, b, c):
            print(m, end=' ')
            time.sleep(0.3)
        print()
    else:
        print(f'contagem regressiva de {a} até {b} de {c} em {c}')
        for m in range(a, b, -c):
            print(m, end=' ')
            time.sleep(0.3)
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('=-'*25)
print('Agora é a sua vez de personalizar a contagem!')
start = int(input('inicio: '))
end = int(input('fim: '))
gap = int(math.sqrt(math.pow(int(input('intervalo: ')), 2)))
contador(start, end, gap)
