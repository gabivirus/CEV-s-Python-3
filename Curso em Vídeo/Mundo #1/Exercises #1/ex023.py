n = int(input('escolha um número de 0 á 9999: '))
n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n//100 % 10
n4 = n//1000 % 10
print(f'seu número {n}')
print(f'unidade {n1}')
print(f'dezena {n2}')
print(f'centena {n3}')
print(f'milhar {n4}')
