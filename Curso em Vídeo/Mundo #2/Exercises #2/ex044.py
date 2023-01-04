price = float(input('Valor do produto: '))

print('Informe a forma de pagamento:')
choice = str(input('À vista? (sim ou não): ')).lower()
x = 10/100*price
a = price - x
y = (20/100*price) + price

if choice == 'sim':
    print(f'Seu desconto é de 10%, e o novo valor é de {a}')
elif choice == 'não':
    choic = int(input('Deseja parcelar?\n Em quantas vezes? '))
    if choic > 2:
        print(f'Parcelando em {choic}x, o juros é de 20%\nAs parcelas são de {y/choic} \nE o preço final é de {y}')
    else:
        print('O valor das parcelas é de {}\nNão houveram alterações no preço'.format(price/choic))
else:
    print('iválido')