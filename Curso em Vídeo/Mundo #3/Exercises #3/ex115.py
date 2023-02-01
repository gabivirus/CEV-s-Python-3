breaker = True
loop = 'yes'

while True:
    try:
        print('=' * 30)
        newPerson = str(input('Insira o nome: '))
        personAge = int(input('Insira a idade: '))
        print('=' * 30)

    except ValueError:
        print('\nOcorreu um erro!')

    except KeyboardInterrupt:
        print('=' * 30)
        print('\nO Programa foi encerrado.')
        print('=' * 30)
        break

    else:
        with open('PeopleData.txt', 'a') as data:
            data.write(f'|\033[35mnome:\033[m {newPerson:<30} \033[35m{personAge:>3}\033[m anos|\n')

        loop = input('\nNova pessoa cadastrada! Deseja continuar? ').lower()
        if loop in 'nonaonão' or not breaker:

            show = input('\nDeseja consultar os dados cadastrados? ').lower()
            if show in 'yesims':

                data = open('PeopleData.txt', 'r')

                print('\n' + '='*50, sep='')
                for line in data:
                    line = line.rstrip()
                    print(line)
                print('='*50)

            break

    finally:
        if loop in 'nonaonão':
            clear = input('\nLimpar dados? ')
            if clear in 'simyes':
                data = open('PeopleData.txt', 'w')
                print('\nOs dados foram limpos.')
                data.close()
            print('\nObrigado')
            break
