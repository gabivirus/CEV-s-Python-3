tupla = (int(input('1°: ')), int(input('2°: ')), int(input('3°: ')), int(input('4°: ')))
par = 0

for c in range(len(tupla)):
    if tupla[c] % 2 == 0:
        par += 1

print(f'O número 9 apareceu {tupla.count(9)} vezes.',
      f'O primeiro três apareceu na posição {tupla.index(3)+1}.',
      f'{par} números pares foram digitados.', sep='\n')
