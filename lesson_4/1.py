from sys import argv


def calc(time, cost, bonus):
    try:
        return f'Your salary is {float(time) * float(cost) + float(bonus)}'
    except ValueError:
        return 'Value error'
    except TypeError:
        return 'Type error'


name, time, cost, bonus = argv
print(calc(time, cost, bonus))





