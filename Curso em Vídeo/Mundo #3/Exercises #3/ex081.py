list = []
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        list.append(n)

print(f'Foram digitados {len(list)} números.')
list.sort(reverse=True)
print(f'Números decrescentes: {list}')
if 5 in list:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')