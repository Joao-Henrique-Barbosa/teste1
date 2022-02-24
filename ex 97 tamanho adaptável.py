def escreva(txt):
    tam = len(txt)+15
    print('~'*tam)
    print(f'{txt:^{tam}}')
    print('~'*tam)


'''
def escreva(txt):
    tam = len(txt)+4
    print('-'*tam)
    print(f"  {txt}")
    print('-'*tam)
'''

word = str(input('Digite uma palavra: '))
escreva(word)
