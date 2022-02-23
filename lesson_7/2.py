from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.__size = size

    @abstractmethod
    def expend(self):
        pass

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 0:
            self.__size = size


class Suit(Clothes):
    def expend(self):
        return round(2 * self.size + 0.3,2)


class Coat(Clothes):
    def expend(self):
        return round(self.size / 6.5 + 0.5,2)


suit = Suit(14)
coat = Coat(10)

print(suit.size)
suit.size = -2
print(suit.size)
suit.size = 10
print(suit.size)


print(coat.expend())
print(suit.expend())
