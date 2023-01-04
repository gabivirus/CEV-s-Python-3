from math import hypot

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da soma dos catetos ({co, ca}) da hipotenusa é de {hi:.2f}')
