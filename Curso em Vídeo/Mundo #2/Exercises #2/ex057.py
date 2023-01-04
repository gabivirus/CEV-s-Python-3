a = str(input('Informe seu sexo [m/f]: ')).lower()
while a not in 'fm':
    a = str(input('Dados errados digite novamente: ')).lower()
if a == 'f':
    print('Seu sexo é feminino.')
if a == 'm':
    print('Seu sexo é masculino.')
print('FIM')
