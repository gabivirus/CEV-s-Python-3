k = int(input('Qual é a distância em Km:'))
close = 0.50*k
far = 0.45*k
if k <= 200:
    print(f'o valor da viagem é de R${close:.2f}')
else:
    print(f'O valor da viagem é de R${far:.2f}')
print('fim')

# com if/else também dá para usar uma só variante para os dois statement, if e else, e depois só simplificar no print
# use se o valor é maior ou menor (</>)
