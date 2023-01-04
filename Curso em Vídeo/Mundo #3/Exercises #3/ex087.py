matrix = []
row = []
even = odd = third = 0

for item in range(3):
    row.clear()
    for index in range(3):
        n = int(input('Digite um número: '))
        row.append(n)
        if n % 2 == 0:
            even += n
        else:
            odd += n
        if index == 2:
            third += n
    matrix.append(row[:])

print('+=+'*30)
print('+=+'*30)
print(f'O soma dos números pares são: {even}. Já dos ímpares: {odd}')
print(f'A soma dos valores da terceira coluna é: {third}')
print(f'O maior valor da segunda linha é: {max(matrix[1])}')
