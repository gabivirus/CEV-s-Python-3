nomedia = []
aluno = []

print('=+='*10, 'Boletim', '=+='*10)

while True:
    nome = input('Digite o nome do alune: ')
    if nome in 'endnonopnot':
        break

    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1+n2)/2


    aluno.append(nome)
    aluno.append(media)
    nomedia.append(aluno[:])
    aluno.clear()

print('Listagem de alunos.')
for n, c in enumerate(nomedia):
    print(f'{n+1}° Alune: {c[0]}\n\033[034mMédia: {c[1]}\033[m\n')

index = int(input('Digite o código do alune que deseja ver: '))
print(f'Alune: {nomedia[index-1][0]}\n\033[34mMédia: {nomedia[index-1][1]}\033[m\n')

