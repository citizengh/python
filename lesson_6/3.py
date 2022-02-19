class Worker:
    name = 'emptyName'
    surname = 'emptySurname'
    position = 'driver'
    _income = {"wage": 1000, "bonus": 250}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Your total income is {self._income["wage"] + self._income["bonus"]}!'


print(Worker.name)
print(Position.name)
print(Position.position)

pos = Position()

pos.name = 'Ivan'
pos.surname = 'Petrov'
pos.position = 'super driver'

print(Worker.position)
print(Position.position)
print(pos.position)

print(pos.get_full_name())
print(pos.get_total_income())
