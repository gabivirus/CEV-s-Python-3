try:
    a = int(input('Nmerador: '))
    b = int(input('Denominador: '))
    r = a/b

except (ValueError, TypeError):
    print('Valor digitado não elegível.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except KeyboardInterrupt:
    print('Digitação de dados interrompida')

else:
    print('Resultado:', r)

finally:
    print('Obrigado')
