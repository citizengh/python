def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Cell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'I have {self.count} cells!'

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if isint(count) and count >= 0:
            self.__count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            print(f'Error')

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        if other.count > 0:
            return Cell(self.count // other.count)

    def make_order(self, count):
        if not isint(count) or count <= 0:
            return
        return '\n'.join(['*' * count for i in range(self.count // count)]) + '\n' + '*' * (self.count % count)


c1 = Cell(21)
c2 = Cell(10)
print(c1.make_order(5))

print(c2 + c1)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)

