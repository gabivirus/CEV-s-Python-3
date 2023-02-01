def coin(value):
    return str(f'R${value:.2f}').replace('.', ',').strip()


def increase(value, percent, show=True):
    value += value * percent / 100
    if show:
        return coin(value)
    else:
        return value


def decrease(value, percent, show=True):
    value -= value * percent / 100
    if show:
        return coin(value)
    else:
        return value


def double(value, show=True):
    value *= 2
    if show:
        return coin(value)
    else:
        return value


def half(value, show=True):
    value -= value * 0.5
    if show:
        return coin(value)
    else:
        return value


print(coin(10.5))
