print('''Progressões Aritméticas
''')
t = int(input('digite o primeiro termo: '))
r = int(input('Digite a razão: '))

n = t + (10 - 1) * r

for c in range(t, n, r):
    print(f'{c} >', end=' ')
print('acabou')
