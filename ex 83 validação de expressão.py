expr = str(input('Digite uma expressão: '))
pilha = []
for p, simb in enumerate(expr):
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('-')
            break
if len(pilha) == 0:
    print('Essa expressão é válida')
else:
    print('Essa expressão é invalida')
