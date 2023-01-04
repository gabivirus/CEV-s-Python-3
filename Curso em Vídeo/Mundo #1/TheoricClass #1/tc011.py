a = 3
b = 5
cores = {'limpa': '\033[m',
         'red': '\033[31m',
         'blue': '\033[33m'}

print(f'Os valores são \033[32;33m{a}\033[m e \033[33;40m{b}\033[m')

print('{} nome {}'.format('\033[33m', '\033[m'))

print('{}nome{}'.format(cores['red'], cores['limpa']))

# para que o background não chegue até o fim da linha adicione outra vez \033[m, ao final da frase para limitar
# função (f'{}' funciona apenas para incluir funções no print, não abrange muitos comandos paara si
