from math import radians, cos, sin, tan

x = float(input('Qual é a medida do angulo? '))
y = radians(x)
a = cos(y)
b = sin(y)
c = tan(y)
print(f'sen = {b:.2f}\n cos = {a:.2f}\n tan = {c:.2f}')
