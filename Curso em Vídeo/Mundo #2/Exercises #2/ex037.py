coin = int(input('Valor para conversão: '))
base = input('''Escolha a base de conversão.
hexa, octa, bina ou all: ''')
hexa = hex(coin)[2:]
octa = oct(coin)[2:]
bina = bin(coin)[2:]
if base == 'hexa':
    print(f'{coin} é igual á:\033[032m {hex(coin)}\033[m Em hexadecimal')
elif base == 'octa':
    print(f'{coin} é igual à:\033[32m {oct(coin)}\033[m Em octal')
elif base == 'bina':
    print(f'{coin} é igual à:\033[32m {bin(coin)}\033[m Em binário')
elif base == 'all':
    print(f'{coin} é igual á: {hexa} em hexadecimal\n {octa} em octal\n {bina} em binário')
