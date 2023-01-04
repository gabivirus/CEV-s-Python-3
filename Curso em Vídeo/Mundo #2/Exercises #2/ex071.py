n100 = n50 = n20 = n10 = n5 = n2 = 0

valor = int(input("Digite o valor que deseja sacar: "))

while True:

    while valor >= 100:
        n100 += 1
        valor -= 100

    while valor >= 50:
        n50 += 1
        valor -= 50

    while valor >= 20:
        n20 += 1
        valor -= 20

    while valor >= 10:
        n10 += 1
        valor -= 10

    while valor >= 5:
        n5 += 1
        valor -= 5

    while valor >= 2:
        n2 += 1
        valor -= 2

    if valor <= 1:
        break

print('SAQUE APROVADO\nAs cédulas cedidas serão', end=': ')

if n100 >= 1:
    print(f'{n100} cédula(s) de R$100')

if n50 >= 1:
    print(f'{n50} cédula(s) de R$50')

if n20 >= 1:
    print(f'{n20} cédula(s) de R$20')

if n10 >= 1:
    print(f'{n10} cédula(s) de R$10')

if n5 >= 1:
    print(f'{n5} cédula(s) de R$5')

if valor == 1:
    print('Restando 1 real, passe no caixa para resgatar\nOu deixe em sua conta corrente')

# if n2 >= 1:
#    print(f'{n2} de R$5')

'''print(f''''''Serão {n100} notas de cem;
{n50} notas de 50;
{n20} notas de 20;
{n10} notas de 10;
{n5} notas de 5;
 e {n2} notas de 2'''''')'''
