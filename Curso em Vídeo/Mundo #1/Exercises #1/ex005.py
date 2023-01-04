n1 = float(input('qual foi a primeira nota?'))
n2 = float(input('e a segunda?'))
n3 = (n1+n2)/2
print('á média das notas do aluno é {:.5f}'.format(n3))

# se usar só um digito no ponto flutuante {:.1f}, o python irá arredondar o número para cima
