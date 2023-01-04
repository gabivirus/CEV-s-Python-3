count = soma = 0
while True:
    a = int(input('Digite um número: '))
    if a == 999:
        break
    else:
        count += 1
        soma += a
print(f'A soma dos {count} valores foi {soma}')
