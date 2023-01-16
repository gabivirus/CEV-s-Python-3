person = dict()
people = list()
woman = list()
elders = list()
count = 0
average = 0

while True:
    count += 1

    print('=-='*15)
    while True:
        identifier = str(input('Digite o nome da pessoa: '))
        if identifier:
            person['name'] = identifier
            break
        else:
            print('Erro. Responda novamente')

    while True:
        identifier = int(input(f"Digite a idade de {person['name']}: "))
        if identifier in range(0, 999):
            person['age'] = identifier
            break
        else:
            print('Erro. Responda novamente')

    while True:
        identifier = str(input(f"E qual o sexo de {person['name']}? [F/M] ")).upper()
        if identifier in 'FM':
            person['sex'] = identifier
            break
        else:
            print('Erro. Responda novamente')

    print('=-='*15)

    average += person['age']
    people.append(person.copy())

    while True:
        q = str(input('\nDeseja continuar cadastrando? '))
        print()
        if q in 'nnaononot':
            print('Muito obrigado!')
            break
        elif q in 'ssimyes':
            break
        else:
            print('Erro. Responda novamente')
    if q in 'nnaononot':
        break

print()
for gender_verify in people:
    if gender_verify['sex'] == 'F':
        woman.append(gender_verify['name'])

print('=-=-'*12, ' Grupo ', '=-=-'*12)
print(f'\nForam cadastradas {count} pessoas.\n')

for index, folk in enumerate(people):
    print(f"{index+1}° {folk['name']}, com {folk['age']} anos de idade. Do sexo {folk['sex']}.\n")
    if folk['age'] > average/count:
        elders.append(folk)

print('=-='*15)
print()
print('A lista da mulheres é:', end=' ')
for girl in woman:
    print(girl, end=', ')

print('\n')
print('=-='*15)
print()
print(f'As pessoas acima da média de {average/count:.0f} são:')
for old in elders:
    print(f"{old['name']}, com {old['age']} anos de idade;")
print()
print('=-='*15)
