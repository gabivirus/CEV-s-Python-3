from random import randint
allBets = []
uniqueBet = []

print('-=-'*10, ' Gerador de apostas! ', '-=-'*10, '\n')

betQuantity = int(input('Quantas apostas deseja gerar? '))

for bet in range(betQuantity):
    for number in range(6):
        while True:
            token = randint(1, 60)
            if token not in uniqueBet:
                uniqueBet.append(token)
                break

    uniqueBet.sort()
    allBets.append(uniqueBet[:])
    uniqueBet.clear()

for position, guess in enumerate(allBets):
    print(f'\n{position+1}° palpite:', end=' ')
    for order in allBets[position]:
        print(order, end=', ')
