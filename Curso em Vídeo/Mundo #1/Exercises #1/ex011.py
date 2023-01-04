name = input('produto: ')
product = float(input('Preço do Produto: '))
value = int(input('Quanto % de desconto? '))
math = value/100*product
descount = product-math
print(f'Com 5% de desconto no produto ({name}). Foi descontado {math:.2f}, o valor final é de {descount:.2f}.')

# cálculo porcentagem % > número da porcentagem / 100 * valor que deve ser caluclado
# ex: se você precisa calcular quanto é 10% de 1000 reais,(ou qualquer outro valor), faça assim
# 10/100*1000 = 100, 10% de 1000 é igual a 100
# 50% de 3000 >>> 50 / 100 * 3000 = 1500
#                  ^    ^      ^___________
# quantidade de desconto/100*valor do produto
