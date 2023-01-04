import random

print('\033[31mJOKENPÔ\033[m')

a = input('Escolha entre\n Pedra\n Papel\n Tesoura: ').capitalize()

x = ['Pedra', 'Papel', 'Tesoura']
y = random.choice(x)

if a == y:
    print(f'Computador \033[31m{y}\n Empate\033[m')
elif a == 'Pedra' and y == 'Tesoura':
    print(f'Computador \033[31m{y}\n Vitória\033[m')
elif a == 'Pedra' and y == 'Papel':
    print(f'Computador \033[31m{y}\n'
          f'Derrota\033[m')
elif a == 'Papel' and y == 'Pedra':
    print(f'Computador \033[31m{y}\n Vitória\033[m')
elif a == 'Papel' and y == 'Tesoura':
    print(f'Computador \033[31m{y}\n'
          f'Derrota\033[m\n')
elif a == 'Tesoura' and y == 'Papel':
    print(f'Computador \033[31m{y} Vitória\033[m\n')
elif a == 'Tesoura' and y == 'Pedra':
    print(f'Computador \033[31m{y}\n'
          f'Derrota')
else:
    print('Jogada invalida')