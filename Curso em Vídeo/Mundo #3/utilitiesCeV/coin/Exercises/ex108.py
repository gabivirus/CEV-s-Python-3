from coin import ex108

number = float(input('Digite um valor: '))
calc = int(input('Digite um valor de porcentagem: '))

print(f'\nO dobro de {ex108.coin(number)} é {ex108.double(number)}')
print(f'A metade de {ex108.coin(number)} é {ex108.half(number)}')
print(f'O cálculo de {calc}% sobre {ex108.coin(number)} é: + {ex108.increase(number, calc)}, - {ex108.decrease(number, calc)}')
