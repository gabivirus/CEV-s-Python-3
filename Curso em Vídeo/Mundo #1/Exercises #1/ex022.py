nome = input('Digite seu nome completo: ')
replace = nome.replace(' ', '')
first = nome.split()
many = first[0]
print(nome.upper())
print(nome.lower())
print('Seu nome completo contém tem', len(replace), 'caracteres')
print('Seu primeiro nome tem', len(many.strip()), 'caractere')
