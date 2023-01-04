num = 0
for c in range(1, 7):
    a = int(input(f'Digite o {c}° valor: '))
    if a % 2 == 0:
        num += a
print(num)
