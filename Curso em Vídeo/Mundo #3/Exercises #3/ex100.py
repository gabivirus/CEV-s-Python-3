from random import randint


numberList = []
evenNumbers = []


def write(message):
    txtlen = len(message)+4
    if txtlen == 0:
        print('A mensagem não pode ser exibida.')
    else:
        print('-'*txtlen)
        print(f'  {message}  ')
        print('-'*txtlen)


def numberSort(numberAmount):
    for sortNumber in range(numberAmount):
        numberList.append(randint(1, 10))


def evenNumberSum(thisList):
    evenSum = 0

    for numberVerifier in thisList:
        if numberVerifier % 2 == 0:
            evenSum += numberVerifier
            evenNumbers.append(numberVerifier)

    print(f'A lista com todos os números é: {numberList}\n')
    print(f'Os números pares são: {evenNumbers}\n')
    print(f'E a soma desses números é {evenSum}\n')


write('Sorteio e identificador de números')
rounds = int(input('\nDigite a quantidade de rodadas: '))
print()

numberSort(rounds)
evenNumberSum(numberList)
