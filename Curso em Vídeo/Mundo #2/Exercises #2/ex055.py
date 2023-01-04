ma = 0
mn = 0
for c in range(1, 6):
    a = float(input(f'Diga o {c}º peso: '))
    if c == 1:
        ma = c
        mn = c
    else:
        if a > ma:
            ma = a
        if a < mn:
            mn = a
print(f'''\033[31mO maior peso é {ma}Kg.
 \033[32mE o menor peso é {mn}Kg.''')
