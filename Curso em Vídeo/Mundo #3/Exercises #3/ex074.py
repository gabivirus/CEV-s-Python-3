from random import randint

menor = maior = 0
number = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

#for c in range(len(number)):
#    if c == 0:
#        maior = menor = number[0]
#    else:
#        if number[c] > maior:
#            maior = number[c]
#        if number[c] < menor:
#            menor = number[c]

print(f'Os números sorteados foram {number}\nO maior número foi: {max(number)}\nE o menor foi {min(number)}')
