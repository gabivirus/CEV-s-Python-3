import random
from random import randint

ns = [0, 1, 2, 3, 4, 5]
y = random.choice(ns)
x = int(input("Escolha entre '0' e '5': "))
if x == y:
    print('Parabéns! Você acertou!')
else:
    print(f'Que pena você errou :( \n o número era na verdade {y}')
print('FIM')

# Com Randint

pc = randint(0, 5)
player = int(input('de 1 a 5'))
if player == pc:
    print('yes')
else:
    print('no')

