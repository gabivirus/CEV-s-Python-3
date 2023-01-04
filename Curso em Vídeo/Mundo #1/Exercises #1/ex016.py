import math
from math import floor, ceil

print('>>>>>>>>>>>>>> Arredondador de Números <<<<<<<<<<<<<<')
n = float(input('digite um número'))
print(f'Seu número alto resumido é {ceil(n)}\n E seu número baixo resumido é {floor(n)}')
print('A porção inteira é {}'.format(math.trunc(n)))

# dá pra fazer de várias formas:
# com math.trunc(X);
# com .format(int(x))
# e com math.floor or .ceil(x)
