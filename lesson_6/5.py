class Stationery:
    title = ''

    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручки!')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандаша!')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркера!')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()

