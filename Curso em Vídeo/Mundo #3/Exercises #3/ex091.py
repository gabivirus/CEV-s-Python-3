from random import randint
from operator import itemgetter
from time import sleep

players = {'player1' : randint(1, 6),
            'player2' : randint(1, 6),
            'player3' : randint(1, 6),
            'player4' : randint(1, 6)}

rank = sorted(players.items(), key  = itemgetter(1), reverse = True)

for k, v in enumerate(rank):
    print(f'{k+1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)
