matrix = []
row = []

for item in range(3):
    row.clear()
    for index in range(3):
        row.append(int(input('Digite um número: ')))
    matrix.append(row[:])

for c in range(3):
    for i in range(3):
        print(f'[{matrix[c][i]:^5}]', end='')
    print()
