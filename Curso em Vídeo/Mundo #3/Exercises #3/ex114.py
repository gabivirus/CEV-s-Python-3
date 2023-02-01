from urllib.request import urlopen

try:
    urlopen("http://www.pudim.com.br")

except Exception as error:
    print('\nO site não está disponível.\n'
          f'O problema é {error}\n')

else:
    print('\nO site está disponível')
    print('Acesse: http://www.pudim.com.br\n')

finally:
    print('Obrigado!')
