class ZeroDivisionEx(Exception):
    def __init__(self, message):
        self.message = message


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise ZeroDivisionEx(f'Делить на 0 нельзя!')
    else:
        print(f'Частное: {a / b}')
except ValueError:
    print('Ошибка ввода данных!')
except ZeroDivisionEx as err:
    print(err.message)
