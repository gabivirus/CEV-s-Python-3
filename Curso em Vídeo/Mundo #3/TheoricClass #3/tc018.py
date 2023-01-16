gols = 0
pe = {'nome':'Gus', 'rod':3, 'partidas':{'partida 1':2, 'partida 2':0},'gols':gols}

print(pe['partidas']['partida 1'])
for k, v in pe['partidas'].items():
    print(k, v)
'''pessoas = []
pessoa1 = {'nome': 'Gabriel', 'idade': 19, 'sexo':'Gosto'}
pessoa2 = {'nome':'Nayara', 'idade': 17, 'sexo': 'Bleh'}

pessoas.append(pessoa1)
pessoas.append(pessoa2)
pessoa2['sexo'] = input('Digite o sexo: ')
pessoa1['altura'] = int(input('Digite a altura: '))

print(pessoa1)
print(pessoas[1]['sexo'])'''
#é necessário aspas diferentas da que se usa no print se usar as aspas
# simples '', então na item, use aspas duplas ""
#
#em print(pessoa[0]) ocorrerá um erro porque não há nada ddefinido como '0'