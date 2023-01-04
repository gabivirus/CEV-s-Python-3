from random import randint

count = 1
players = {}
player = []

for c in range(1, 5):
    players[f'{c}° Jogador'] = randint(0, 6)
    if c == 1 or players[f'{c}° Jogador'] > player[-1]:
        player.append(players[f'{c}° Jogador'])
    else:
        p = 0
        while p < len(player):
            if players[f'{c}° Jogador'] <= player[p]:
                player.insert(p, players[f'{c}° Jogador'])
                break
            p += 1

print()
for k in range(1, 5):
    print(f"em {k}° lugar, com {player[k-1]['{k}° jogador']} no dado ficou o {player[k]}")

print()

