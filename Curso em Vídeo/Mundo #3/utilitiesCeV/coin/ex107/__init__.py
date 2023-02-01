def increase(value, percent):
    value += value * percent / 100
    return value


def decrease(value, percent):
    value -= value * percent / 100
    return value


def double(value):
    value *= 2
    return value


def half(value):
    value -= value * 0.5
    return value
