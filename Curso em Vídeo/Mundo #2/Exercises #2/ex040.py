a = float(input('primeira nota: '))
b = float(input('segunda nota: '))
c = (a + b)/2
print(f'sua média é {c}')
if c > 6.9:
    print('Aprovado')
elif c > 4.9 < 7.0:
    print('Recuperação')
elif c < 5.0:
    print('Reprovado')
