numbers = [[], []]

print('Separador e Organizador de Númerais.')

for c in range(1, 8):
    n = input('Digite um o {c}° número: ')
    if int(n) % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

numbers[0].sort()
numbers[1].sort()

print(f'Os números pares são {numbers[0]}')
print(f'E os búmeros ímpares são {numbers[1]}')
