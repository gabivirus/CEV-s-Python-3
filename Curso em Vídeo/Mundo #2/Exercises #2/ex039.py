from datetime import date
print('\033[32mCHECAGEM DE ALISTAMENTO!')

ano = int(input('Diga seu ano de nascimento: '))

age = date.today().year - ano
anos = 17 - age
pas = age - 18

print(f'Você tem {age} anos')

if age < 18:
    print(f'Ainda faltam {anos} anos para o seu alistamento.')
elif 17 < age < 19:
    print('Está na hora de se alistar.')
elif 18 < age > 18:
    print(f'Seu tempo de alistamento passou a {pas} anos')
