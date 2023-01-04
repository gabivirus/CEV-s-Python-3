while True:
    aluno = {}

    print('_'*30)
    aluno['nome'] = input('\nDigite o nome do aluno: ')
    aluno['média'] = int(input(f'Digite a média de {aluno["nome"]}: '))
    print('_'*30)

    if aluno['média'] >= 5:
        aluno['situ'] = 'Aprovado'
    else:
        aluno['situ'] = 'Reprovado'

    print('_'*30)
    print(f'\nO alune {aluno["nome"]} teve a média {aluno["média"]} e foi {aluno["situ"]}')
    print('_'*30)

    q = input('\nDeseja continuar? ')
    if q in 'nonnopnaonãoNÃONONNOPNAONOTnot':
        break
