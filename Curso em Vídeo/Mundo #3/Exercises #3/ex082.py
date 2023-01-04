#não criar múltiplas listas em uma só linha 'a = b = c = []
par = []
imp = []
list = []

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    else:
        list.append(n)

for c in range(len(list)):
    if list[c] %2 == 0:
        par.append(list[c])
    else:
        imp.append(list[c])

print(f'Valores digitados: {list}')
print(f'Valores Pares: {par}')
print(f'Valores Impares: {imp}')
