from time import sleep

allPlayers = []
qna = False

while True:
    joga = {}
    play = {}
    gols = 0

    joga['nome'] = str(input('Digite o nome do jogador: '))
    joga['rod'] = int(input(f'Digite quantas partidas {joga["nome"]} jogou?: '))

    print('\n')
    print('Agora a quantidade de gols por partida.\n')

    for c in range(1, joga['rod']+1):
        play[c] = int(input(f'Partida n° {c}: '))
        joga['gols'] = gols
        gols += play[c]

    print('\n')
    for k, v in play.items():
        print(f'Na {k}° partida, {joga["nome"]} marcou {v} gols.')
        sleep(1)

    print(f'Com um total de {gols} gols no campeonato.')

    joga['partidas'] = play
    allPlayers.append(joga.copy())

    q = str(input('\nDeseja continuar analisando jogadores? '))
    if q in 'nnaononot':
        print('\nMuito obrigado!\n')
        break

while True:
    print('Overview\nOs jogadores são:', end=' ')

    while True:
        qna = False 
        for nm in allPlayers:
            print(nm['nome'], end=', ')
        name = str(input('\nQual jogador você quer ver? '))

        for qn in allPlayers:
            if name == qn['nome']:
                qna = True
                break
            
        if qna:
            break
        else:
            print('Esse jogador não foi inscrito. Por favor, tente novamente')

    for k in allPlayers:
        if k['nome'] == name:
            print(f'\nO jogador {name} jogou {k["rod"]} jogos, pontuando um total de {k["gols"]} gols.')
            print('E esses foram os resultados das rodadas:')
            for w, e in k['partidas'].items():
                print(f'Partida {w}: {e}')
        print('\n')

    q = str(input('\nDeseja continuar analisando jogadores? '))
    if q in 'nnaononot':
        print('\nMuito obrigado!\n')
        break
