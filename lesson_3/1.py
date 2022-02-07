def divide(d1, d2):
    """d1 - делимое, d2 - делитель """
    if d2 == 0:
        print("На 0 делить нельзя!")
        return
    return d1 / d2


def input_digit(mes='Введите число:'):
    """Используется для ввода чисел"""
    d = ""
    while not d.isdigit():
        d = input(mes)
    return float(d)


d1 = input_digit('Введите 1-е число:')
d2 = input_digit('Введите 2-е число:')

print('Частное =',round(divide(d1, d2),6))
