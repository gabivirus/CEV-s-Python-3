a = float(input('primeira reta: '))
b = float(input('segunda reta: '))
c = float(input('terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo')
    if a == b == c:
        print('Equilátero')
    elif a == b != c or a == c != b or b == c != a:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não é possível formar um triângulo')
