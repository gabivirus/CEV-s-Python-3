def readInt(value):
    ok = False
    number = 0
    while True:
        integerNum = str(input(value))

        if integerNum.isnumeric():
            number = int(integerNum)
            ok = True

        else:
            print('\033[31mERRO! Digite um número válido.\033[m')
        
        if ok:
            break
    
    return number


integer = readInt('Digite um número: ')

print(f'O número que você digitou foi: {integer}')
