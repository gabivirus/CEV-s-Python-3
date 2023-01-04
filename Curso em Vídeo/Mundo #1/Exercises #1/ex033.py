print('Diga três números:')
a = int(input('1° número:'))
b = int(input('2° número:'))
c = int(input('3° número:'))
menor = a
maior = a
if a > b and c:
    maior = a
if b > a and c:
    maior = b
if c > a and b:
    maior = c
if a < b and c:
    menor = a
if b < a and c:
    menor = b
if c < b and a:
    menor = c
print(menor)
print(maior)

# another way

print('Diga três números:')
a = int(input('1° número:'))
b = int(input('2° número:'))
c = int(input('3° número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'o menor valor é: {menor}')
print(f'O maior valor é : {maior}')