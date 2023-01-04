c = int
while c != 5:
    a = int(input('Escolha um número: '))
    b = int(input('Escolha um número: '))
    c = 0
    while c < 4:
        if c < 4:
            c = int(input('''Qual operação deseja realizar?
            [1]somar;
            [2]multiplicar;
            [3]maior;
            [4]novos números;
            [5]sair do programa;
            informe: '''))
            if c == 1:
                print(f'A soma de {a} mais {b} é:', a+b)
            elif c == 2:
                print(f'{a} vezes {b} é igual a: {a*b}')
            elif c == 3:
                if a > b:
                    print(f'{a} é o maior número')
                else:
                    print(f'{b} é o maior número')
print('FIM')
