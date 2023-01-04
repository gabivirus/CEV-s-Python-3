cbf = ('PAL', 'INT', 'FLU', 'COR', 'FLA', 'CAP', 'CAM', 'FOR', 'SAO', 'AME',
       'BOT', 'SAN', 'GOI', 'GBT', 'CFC', 'CUI', 'CEA', 'ACG', 'AVA', 'JUV')

for c in range(len(cbf)):
    if cbf[c] == 'SAO':
        alt = c

print('=' * 20, 'BRASILEIRÃO', '=' * 20, end='\n\n')
print(f'Os primeiros 5 colocados são {cbf[:5]}',
      f'Os últimos colocados da tabela são {cbf[-5:]}',
      f'Em ordem alfabética são {sorted(cbf)}',
      f'O São Paulo está na {cbf.index("SAO")+1}ª posição ', sep='\n{}\n'.format('='*60))
