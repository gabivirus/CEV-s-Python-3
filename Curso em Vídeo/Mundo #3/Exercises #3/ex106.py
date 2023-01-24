def asker(function):
    help(function)


def write(message = ''):
    txtlen = len(message) + 4

    print('~'*txtlen)
    print(f'  {message}  ')
    print('~'*txtlen)


while True:
    write('Sistema de ajuda PyHelp')
    command = str(input('\nFunção ou Biblioteca: '))
    if command.upper() == 'FIM':
        break
    else:
        asker(command)

write('Obrigado')
