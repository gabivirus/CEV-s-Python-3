def write(message):
    txtlen = len(message) + 4

    if txtlen == 0:
        print('A mensagem não pode ser exibida.')

    else:
        print('~'*txtlen)
        print(f'  {message}  ')
        print('~'*txtlen)


msg = str(input('Digite uma mensagem: '))

write(msg)
