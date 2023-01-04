from time import sleep

count = countMin = countMan = countWom = 0

while True:

    count += 1
    print('='*30)
    sexo = input('Informe seu sexo [F/M]: ').lower()
    idade = int(input('Informe sua idade: '))
    print('=' * 30)
    if idade > 18:
        countMin += 1

    if sexo == 'f':
        if idade <= 20:
            countWom += 1
    else:
        countMan += 1
    dec = input('Deseja continuar a cadastrar? ')
    print('=' * 30)
    print('Processing...')
    sleep(2)

    if dec in 'nonãonaon':
        break

if count >= 2:
    print(f'''\nForam cadastradas {count} pessoas.
    {countMin} delas são maiores de 18
    {countMan} é(são) homem(s)
    {countWom} mulher(es) tem menos de 20 anos''')
