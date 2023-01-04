from random import randint

count = 0
while True:
    while True:
        mach = randint(0, 10)
        quest = str(input('PAR OU ÍMPAR? ')).strip
        player = int(input('Escolha um número: '))
        result = mach + player
        if quest == 'par':
            if result % 2:
                print(f'O computador escolheu {mach} dando o total de {result}')
                print('Você Ganhou')
                count += 1
            else:
                print(f'O computador escolheu {mach} dando o total de {result}')
                print('Você perdeu')
                break
        else:
            if result % 2:
                print(f'O computador escolheu {mach} dando o total de {result}')
                print('Você perdeu')
                break
            else:
                print(f'O computador escolheu {mach} dando o total de {result}')
                print('Você Ganhou')
                count += 1
    if count >= 2:
        print(f'Você conseguiu {count} vitórias consecutivas!')
    elif count == 1:
        print('Você consegui apenas umas vitória!')
    else:
        print('Você não ganhou nenhuma vez :(')
        a = input('Deseja jogar novamente? [y/n]')
        if a == 'n':
            break
print(result, result % 0, mach, sep=' > ')
