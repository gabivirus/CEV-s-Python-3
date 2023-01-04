exp = str(input('Digite uma expressão: '))
count = 0
pl = []

for i in range(len(exp)):
    if exp[i] == '(':
        pl.append('(')
    elif exp[i] == ')':
        if len(pl) > 0:
            pl.pop()
        else:
            pl.append(')')
            break

if len(pl) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está errada.')  
