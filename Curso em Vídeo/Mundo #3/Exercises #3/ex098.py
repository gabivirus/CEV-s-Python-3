def counter(start, step, end):

    if step < 0:
        step *= -1
    if step == 0:
        step += 1
    if start > end:
        step *= -1
        end -= 1
    else:
        end += 1

    print(f'\nDe {start} até {end} pulando de {step} em {step}:')
    for number in range(start, end, step):
        print(f'\033[32m{number}\033[m', end=' > ')
    print('Fim!\n')


counter(1, 1, 10)
counter(10, 2, 0)

inicio = int(input('Digite o valor de começo: '))
fim = int(input('Digite o valor de encerramento: '))
passo = int(input('Digite o valor do passo: '))

counter(inicio, passo, fim)
