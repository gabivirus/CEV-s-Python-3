y = 'yes'
menor = 999
maior = m = n = med = count = 0
while y == 'yes':
    count += 1
    n = int(input('Diga um número inteiro: '))
    y = str(input('Deseja continuar classificar números? '))
    med += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    m += n
print(f'Você digitou {count} números')
print('A média entre os números é ', m/med)
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
