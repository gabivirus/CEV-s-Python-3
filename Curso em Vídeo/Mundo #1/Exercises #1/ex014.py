print('        Calculador de preço de Aluguel automotivo')
km = int(input("Quantos Km's foram percorridos? "))*0.15
day = int(input('Por quantos dias foi alugado? '))*60
val = km+day
print(f'O total do aluguel do carro, por dias usados e km´s percorridos, equivalem à R${val:.2f}.')
