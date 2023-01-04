from time import sleep

pdt = ''
count = cost = total = minor = 0
while True:
    print('='*30)
    name = str(input('Informe o nome do produto: ')).strip().capitalize()
    price = int(input('Informe o preço do produto: '))
    print('=' * 30)
    cost += price
    count += 1
    se = str(input('Deseja continuar? ')).lower()
    print('=' * 30)
    print('Processing...')
    print('=' * 30)
    sleep(2)
    if price >= 1000:
        total += 1
    if count == 1 or price < minor:
        minor = price
        pdt = name
    if se == 'não' or se == 'not' or se == 'n':
        break
print('='*15, ' FIM DO PROGRAMA ', '='*15)
print('='*30)
print(f'\n\033[031m O total gasto na compra é de {cost}\n {total} Produtos custam mais de R$1000'
      f'\nE o produto mais barato foi {pdt}, custando R${minor}')
print('='*30)
