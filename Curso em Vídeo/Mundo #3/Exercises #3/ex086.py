matrix = []
row = []

for item in range(3):
    row.clear()
    for index in range(3):
        row.append(int(input('Digite um número: ')))
    matrix.append(row[:])

print(matrix[0], matrix[1], matrix[2], sep='\n')
