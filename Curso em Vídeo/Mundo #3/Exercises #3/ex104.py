def readInt(value):
    ok = False
    number = 0
    while True:
        integer = str(input(value))

        if integer.isnumeric():
            number = int(integer)
            ok = True

        else:
            '\033[31mERRO! Digite um número válido.\033[m'
        
        if ok:
            break
    
    return number


integer = readInt('Digite um número: ')

print(f'O número que você digitou foi: {integer}')
