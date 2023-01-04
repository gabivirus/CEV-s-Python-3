list = []

print('Valores')

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    elif n in list:
        print('Esse valor já foi digitado.')
    else:
        list.append(n)

list.sort()
print(list)
