# a = 0
# b = 0
# c = 0
# soma = 0
# while a != 999:
#    a = int(input('Diga um número: ')
#    if a != 999:
#        b += a
#        soma = b + c
#        c += 1
# print(f'Você digitou {c} números, e a soma entre eles é de {soma}')

a = b = c = soma = 0
while a != 999:
    a = int(input('Diga um número: '))
    if a != 999:
        b += a
        soma = b
        c += 1
print(f'Você digitou {c} números, e a soma entre eles é de {soma}')
