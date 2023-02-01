from ex097 import write


def readInt(value):
    number = 0

    newValue = str(input(value))
    number += int(newValue)

    return number


while True:
    try:
        write('Identificador de interiros')
        read = readInt('\nDigite um número: ')

    except ValueError:
        write('\033[31mO valor informado não é um número inteiro válido.')

    except KeyboardInterrupt:
        write('Programa interrompido pelo usuário.')
        break

    except Exception as error:
        write(f'Erro {error}')

    else:
        write(f'O valor digtado foi: {read}')
