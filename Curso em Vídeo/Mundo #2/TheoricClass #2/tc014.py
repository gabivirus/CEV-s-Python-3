a = int
b = -1
c = 0
while a != 0:
    a = int(input('digite um número: '))
    if a % 2 == 0:
        b += 1
    else:
        c += 1
print(f'Você digitou {b} números pares e {c} números ímpares')
print('fim')
