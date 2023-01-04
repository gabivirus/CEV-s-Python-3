a = str(input('Diga uma frase: ')).strip().upper()
b = a.split()
d = ''.join(b)
p = ''
for c in range(len(d) - 1, -1, -1):
    p += d[c]
print(f'O contrário de \033[31m{d}\033[m é \033[35m{p}\033[m')
if p == d:
    print(f'\033[33m{a}\033[m É um palíndromo')
else:
    print(f'\033[33m{a}\033[m não é um palíndromo')
