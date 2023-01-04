numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')

user = int(input('Digite um número de um à vinte: '))

if 0 <= user <= 20:
    print('O número {}, por extenso é: {}'.format(user, numbers[user]))
else:
    print('Valor não encontrado!')
