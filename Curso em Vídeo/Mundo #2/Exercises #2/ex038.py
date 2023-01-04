a = int(input('Digite o primeiro número: '))
b = int(input('Agora o segundo: '))

if a > b:
    print(f'\033[32mO primeiro valor ({a}), é maior!\033[m')
elif b > a:
    print(f'\033[33mO segundo valor ({b}), é o maior\033[m')
elif a == b:
    print('\033[34mOs dois valores são iguais!\033[m')