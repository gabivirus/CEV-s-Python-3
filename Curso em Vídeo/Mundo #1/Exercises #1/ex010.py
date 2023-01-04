altura = float(input('Qual a altura da parede que desejas cálcular'))
largura = float(input('Qual a largura da parede que desejas cálcular'))
area = altura*largura
tinta = round(area/2)
print(f'''A dimensão é de {altura}x{largura}.
A área da parede é de {area:.2f}m².
E a quantidade de tinta necessária é de {tinta:.1f} litros''')
