age = int(input('Informe sua idade: '))

if age < 10:
    print('Atleta Mirim')
elif 9 < age < 15:
    print('Atleta Infantil')
elif 14 < age < 20:
    print('Atleta Júnior')
elif 19 < age < 26:
    print('Atleta Sênior')
elif 25 < age < 50:
    print('Atleta Master')
else:
    print('Que isso cara????')
