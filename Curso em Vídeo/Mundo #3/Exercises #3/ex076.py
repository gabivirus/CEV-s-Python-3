pdt = ('Geleia', 2.50, 'Arroz', 10.98, 'Celular', 1.459, 'Faca', 9.00, 'Pulseira', 0.59)

print(f'\nTabela de produtos\n')

for c in range(0, len(pdt), 2):
    print(f'{pdt[c]:.<30}R${pdt[c+1]:>8}')

print('\n')
