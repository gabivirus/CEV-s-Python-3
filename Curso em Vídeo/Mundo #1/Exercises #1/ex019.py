from random import choice

a1 = str(input('Aluno 1: '))
a2 = str(input('aluno 2: '))
a3 = str(input('aluno 3: '))
a4 = str(input('aluno 4: '))
lista = [a1, a2, a3, a4]
one = choice(lista)
print('Quem irá apagar a lousa é o {}'.format(one))

# listas são entre colchetes []
