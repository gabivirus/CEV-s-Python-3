from coin import ex109

number = float(input('Digite um valor: '))
calc = int(input('Digite um valor de porcentagem: '))

print(f'\nO dobro de {ex109.coin(number)} é {ex109.double(number, False)}')
print(f'A metade de {ex109.coin(number)} é {ex109.half(number)}')
print(f'O cálculo de {calc}% sobre {ex109.coin(number)} é:'
      f' + {ex109.increase(number, calc)}, - {ex109.decrease(number, calc)}')
