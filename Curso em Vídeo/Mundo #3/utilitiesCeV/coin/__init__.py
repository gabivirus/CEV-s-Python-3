def coin(value):
    return str(f'R${value:.2f}').replace('.', ',').strip()


def increase(value, percent, show=True):
    value += value * percent / 100
    return coin(value) if show else value


def decrease(value, percent, show=True):
    value -= value * percent / 100
    return coin(value) if show else value


def double(value, show=True):
    value *= 2
    return coin(value) if show else value


def half(value, show=True):
    value -= value * 0.5
    return coin(value) if show else value


def resume(value, percent):
    print('--'*20)
    print(f'Valor analisado{coin(value):.>20}')
    print(f'Dobro do preço\t{double(value):.>20}')
    print(f'Metade do preço{half(value):.>20}')
    print(f'{percent}% de aumento\t{increase(value, percent):.>20}')
    print(f'{percent}% de desconto{decrease(value, percent):.>20}')
    print('--'*20)
