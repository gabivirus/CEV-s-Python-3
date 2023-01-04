a = 0
s1 = 0
v = 0
no = ''
v1 = 0
for c in range(1, 5):
    print(f'________{c}º pessoa_______')
    n = str(input('\033[34mDiga o nome: ')).capitalize()
    i = int(input('Diga a idade: '))
    s = str(input('Diga o sexo: ')).strip().lower()
    a += i
    if s == 'f' and i < 20:
        s1 += 1
    if c == 1 and s == 'm':
        v = i
    if s == 'm' and i > v:
        v1 = i
        no = n
m = a/4
print(f'\033[31mA média de idade do grupo é {m}')
print(f'\033[32mO homem mais velho é: {no}, com {v1} anos')
print(f'\033[33m{s1} Mulheres tem menos de 20 anos')
