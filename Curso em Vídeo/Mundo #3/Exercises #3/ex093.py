from time import sleep

jogador = {}
gols = []

jogador['nome'] = str(input('Digite o nome do jogador: '))
rod = int(input(f'Digite quantas partidas {jogador["nome"]} jogou?: '))
jogador['gols'] = gols
jogador['total'] = 0

print('\nAgora a quantidade de gols por partida.\n')

for c in range(1, rod+1):
    gol = int(input(f'Partida n° {c}: '))
    jogador['total'] += gol
    gols.append(gol)

print()
for key, values in jogador.items():
    print(f'O campo {key} tem o valor {values}')

print()
for i in range(rod):
    print(f'Na partida {i+1}, {jogador["nome"]} marcou {jogador["gols"][i]} gols.')
    sleep(1)

print()

print(f'Com um total de {jogador["total"]} gols no campeonato.')
