def coin(value):
    return str(value).replace('.', ',').strip()


def increase(value, percent):
    value += value * percent / 100
    return coin(value)


def decrease(value, percent):
    value -= value * percent / 100
    return coin(value)


def double(value):
    value *= 2
    return coin(value)


def half(value):
    value -= value * 0.5
    return coin(value)
