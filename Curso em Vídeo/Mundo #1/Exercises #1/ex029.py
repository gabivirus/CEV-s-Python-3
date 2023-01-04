v = int(input('Qual a velocidade do carro em km: '))
x = v-80
y = x*7
if v > 1:
    print(f'o valor da multa é de R${y}')

else:
    print('tá safe irmão')

# lembrar de fazer os valores e contas dentro do if statement para economizar memória
