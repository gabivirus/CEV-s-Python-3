s = int(input('Informe o valor do salário em R$:'))
x = 15/100*s
y = 10/100*s
if s <= 1250:
    print(f'O seu salário agora é de: {x+s:.2f}')
else:
    print(f'O seu salário agora é de: {y+s:.2f}')
