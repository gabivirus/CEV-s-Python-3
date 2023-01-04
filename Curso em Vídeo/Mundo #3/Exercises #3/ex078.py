list = []
ma = mi = 0

for c in range(5):
      list.append(int(input(f'{c+1}º: ')))
      if c == 0:
            ma = mi = list[c]
      else:
            if list[c] > ma:
                  ma = list[c]
            elif list[c] < mi:
                  mi = list[c]

print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi {ma}, nas posições', end=': ')
for i, v in enumerate(list):
      if v == ma:
            print(i+1,'...', end=' ', sep='')
print(f'\nO menor valor digitado foi {mi}, nas posições', end=': ')
for i, v in enumerate(list):
      if v == mi:
            print(i+1,'...', end=' ', sep='')

'''
mi = list.index(min(list))
ma = max(list)

print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi {ma}, na posição {list.index(ma)+1}... {list.index(ma:-1)+1}')
print(f'O menor valor digitado foi {mi}, na posição {list.index(mi)+1}... {list.index(min(list[list.index(min(list)):-1]))+1}')
'''