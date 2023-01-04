print('(: TABUADAS NA CARA :)\n')

while True:
    while True:
        fator = int(input('Digite um número: '))
        print('='*15)
        if fator < 0:
            break
        else:
            for c in range(1, 11):
                print(f'{fator} x {c} = {fator*c}')
            print('='*15)
    print('Você digitou um número negativo!')
    quest = input('Deseja continuar? [y/n] ').lower
    if quest != 'y':
        break
