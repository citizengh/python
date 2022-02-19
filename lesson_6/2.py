class Road:
    _length = 0
    _width = 0

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calc(self):
        print(f'{round(self._length * self._width * 25 * 5/1000,2)} т.')


road = Road(5000, 20)
road.calc()
