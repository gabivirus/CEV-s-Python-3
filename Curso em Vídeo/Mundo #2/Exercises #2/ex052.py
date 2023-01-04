print('\033[31m Números primos\033[m')

a = int(input('Diga um número: '))
b = 0

for c in range(1, a + 1):
    if a % c == 0:
        print('\033[31m', c, end=' ')
        b += 1
    else:
        print('\033[32m', c, end=' ')

if b == 2:
    print('\033[34mÉ um número primo!')
else:
    print('\033[34mNão é um número primo!')
