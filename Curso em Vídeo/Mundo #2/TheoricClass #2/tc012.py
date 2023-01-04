nome = str(input('Qual seu nome? ')).capitalize()

if nome == 'Gustavo':
    print('\033[35m Que nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'João':
    print('Meu Deus!')
elif nome in 'Maria Julia Ana':
    print('Belo nome feminino!')
else:
    print('Seu Nome é bem normal.')
print(f'tenha um bom dia,\033[32m {nome}\033[m!')
