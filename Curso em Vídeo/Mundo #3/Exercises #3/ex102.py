def myFactorial(facNumber, show='no'):
    '''Esta def calcula e exibe o valor de um número fatórial
    nos parâmetros devem ser um número e na segunda opção
    sim/yes, caso você queira ver o cálculo. Não é obrigatório'''
    
    fac = facCalc = facNumber
    if show in 'yessims':
        while facNumber > 1:
            print(facNumber, end=' x ')
            facNumber -= 1
            facCalc *= facNumber
        return f'1 = {facCalc}'
    else:
        while facNumber > 1:
            facNumber -= 1
            facCalc *= facNumber
        return f'O fatorial de {fac} é: {facCalc}'


print(myFactorial(5))
help(myFactorial)
