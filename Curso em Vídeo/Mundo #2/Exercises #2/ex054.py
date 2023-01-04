from datetime import date

d = 0
b = 0

for c in range(7):
    a = int(input('Diga o ano de nascimento: '))
    if date.today().year - a > 17:
        d += 1
    else:
        b += 1

if d == 1:
    print(f'\033[31m apenas {d} deles é adulto e os outros {b}, ainda não')
else:
    print(f'\033[31m {d} deles já são adultos e {b}, ainda não')
