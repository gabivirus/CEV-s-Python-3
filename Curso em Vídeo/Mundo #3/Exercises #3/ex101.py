from datetime import datetime


age = 0
actualYear = datetime.now().year


def vote(year):
    age = actualYear - year
    if 17 < age < 65:
        return "Obrigatório"

    elif 0 < age < 18:
        return "Negado"
    
    else:
        return 'Opcional'


while True:
    print('-='*20)
    birthYear = int(input('\nInforme seu ano de nascimento: '))
    print('-='*20)

    print(f'\nCom {actualYear - birthYear} anos, a situação do seu voto é: {vote(birthYear)}\n')
    print('-='*20)
