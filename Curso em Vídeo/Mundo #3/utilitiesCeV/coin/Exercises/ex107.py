from coin import ex107

number = int(input('Digite um valor: '))
calc = int(input('Digite um valor de porcentagem: '))

print(f'\nO dobro de {number} é {ex107.double(number)}')
print(f'A metade de {number} é {ex107.half(number)}')
print(f'O cálculo de {calc}% sobre {number} é: + {ex107.increase(number, calc)}, - {ex107.decrease(number, calc)}')
