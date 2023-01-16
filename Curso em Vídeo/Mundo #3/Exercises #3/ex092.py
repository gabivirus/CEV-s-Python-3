from datetime import datetime

ctps = 0
person = {}
actualYear = datetime.now().year

person['name'] = str(input('Informe o nome da pessoa: '))
person['born'] = int(input(f'Informe o ano de nascimento de {person["name"]}: '))
person['age'] = actualYear - (person['born'])

person['ctps'] = str(input('\nInforme também, a carteira de trabalho: '))

if person['ctps'] != '0':
    person['contractYear'] = int(input('\nInforme o ano de contratação: '))
    person['wage'] = int(input('\nInforme o salário: '))

    retireAge = (int(person['contractYear']) + 35) - person['born']

for k, v in person.items():
    print(f' - {k} tem valor {v}')