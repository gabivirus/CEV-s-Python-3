numbers = []
odd = []
even = []

print('Separador e Organizador de Númerais.')

numbers.append(even)
numbers.append(odd)

while True:
    n = input('Digite um número: ')
    if n in 'nonnaonãonopnotNONOPNAONÃONOT ':
        break
    else:
        if int(n) % 2 == 0:
            even.append(int(n))
        else:
            odd.append(int(n))

numbers[0].sort()
numbers[1].sort()

print(f'Os números pares são {numbers[0]}')
print(f'E os búmeros ímpares são {numbers[1]}')
