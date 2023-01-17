from time import sleep


def printL():
    print()
    print('=-' * 20)


def great(* values):
    greater = position = 0

    printL()
    print('Os valores digitados foram:')

    for index, number in enumerate(values):
        print(number, end=' ', flush=True)
        if index == 0:
            greater = number
            position = index

        elif number > greater:
            greater = number
            position = index
        sleep(0.3)

    print('Fim')
    sleep(0.5)
    print(f'\nForam informados {len(values)} ao todo')
    sleep(0.7)
    print(f'\nO maior valor foi: \033[34m{greater}\033[m na \033[34m{position+1}°\033[m posição')
    sleep(1.5)


great(2, 9, 4, 5, 7, 1)
great(4, 7, 0)
great(1, 2)
great(0)
great()
