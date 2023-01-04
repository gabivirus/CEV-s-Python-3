import random
n1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = random.choice(n1)
print('JOGO DA ADIVINHAÇÃO')
g = int(input('Escolha um número de 0 à 10: '))
jog = 1
while g != m:
    jog += 1
    if g > m:
        g = int(input('Menor, Tente novamente: '))
    else:
        g = int(input('Maior, Tente novamente: '))
if g > 2:
    print(f'Parabéns você acertou com {jog} tentativas!')
else:
    print('Você acertou de primeira parabéns!')
