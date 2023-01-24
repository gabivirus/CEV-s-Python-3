def write(message):
    txtlen = len(message) + 4

    if txtlen == 0:
        print('A mensagem não pode ser exibida.')

    else:
        print('~'*txtlen)
        print(f'  {message}  ')
        print('~'*txtlen)


def coin(player='Desconhecido', score=0):
    return write(f'O jogador {player} marcou {score} pontos')


name = str(input(('Nome do jogador: ')))
gols = str(input('Quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if name.strip() == '':
    coin(score = gols)
else:
    coin(name, gols)
