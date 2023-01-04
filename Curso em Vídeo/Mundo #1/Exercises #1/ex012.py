name = input('Nome do Funcionário: ')
wage = float(input('Valor salarial R$'))
promo = 15/100*wage
value = wage+promo
print(f'''Parabéns {name}! Você recebeu uma promoção de 15%. Equivalente a R${promo:.2f}.
Agora seu salário é de R${value:.2f}''')
