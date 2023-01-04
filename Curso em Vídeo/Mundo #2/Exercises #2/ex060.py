print('Números Fatoriais')
fat = int(input('Escolha um número: '))
mult = fat
while fat != 1:
    fat -= 1
    mult += mult * (fat-1)
    print(f"{mult}x{fat}={mult}", end=" ")
