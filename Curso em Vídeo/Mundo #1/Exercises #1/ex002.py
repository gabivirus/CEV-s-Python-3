

# dentro das chaves {}, no print, é possível adicionar funções como;
# :>/< que coloca a informação a direita ou à esquerda da linha
# :10 põem a informação com determinado espaço, 10, 20, 100
# :^ centraliza a informação na linha
# :*^, qualquer sinal antes do circunflexo irá preencher o espaço vazio
#

# lembrando que sempre deve conter dois pontos (:) antes da informação na chave, dentro dela.

n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, a multiplicação vale é {}, a divisão é {:.3f} '.format(s, m, d), end='/// ')
print('divisão inteira {} e potência {}'.format(di, e))

# se eu quiser formatar as casas decimais digito dentro da chave do número que irá
# ser formatado, assim: {:.3f}

# para a linha de um print não ser quebrada ou ser personalizada use no final do parenteses
# , end='') para a linha não acabar
# ou dentro do espaço vazio colloque informações para aparecerem no final daquele print

# e para definir a quebra da llinha sem precisar criar outro print,
# digite \n, contra-barra n, e a linha vai quebrar ali

# usar uma variavel para a soma só é necessário se você for usar essa soma denovo no seu código

