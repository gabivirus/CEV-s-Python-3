def calcArea(wide, lens):
    area = wide*lens
    print(f'A área de {wide}x{lens} é igual a: {area}²')


width = float(input('Informe a largura: '))
length = float(input('Informe o comprimento: '))

calcArea(width, length)
