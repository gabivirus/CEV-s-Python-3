house = int(input('\033[31mDiga o valor da casa R$:\033[m '))
wage = int(input('\033[32mInforme o seu salário R$:\033[m '))
bill = int(input('\033[33mE agora, o número de parcelas em anos R$:\033[m '))*12

x = 30/100*wage
parcel = house / bill

if parcel < x:
    print('Seu empréstimo foi aprovado!')
    print(f'O valor das parcelas é de: \033[32mR${parcel:.5}\033[m')
else:
    print(f'''Infelizmente sua compra não pode ser aprovada.
    O valor das parcelas é de \033[31mR${parcel:.5}\033[m e excede 30% do seu salário que é de:
    R${wage}''')
