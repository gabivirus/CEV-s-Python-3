nome = str(input('digite seu nome completo: ')).strip()
s = nome.split()
print(f'''o primeiro nome é: {s[0]}
e o último nome é {s[-1]}''')
