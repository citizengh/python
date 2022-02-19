class Car:
    speed = 0
    color = ''
    name = ''
    is_police = bool(0)
    __is_motion = bool(0)

    def __init__(self, s, c, n, is_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = is_p

    def go(self):
        print(f'{self.name} goes')
        self.__is_motion = 1

    def stop(self):
        print(f'{self.name} stops')
        self.__is_motion = 0

    def turn(self, direction):
        if self.__is_motion:
            print(f'{self.name} turns {direction}')
        else:
            print(f"{self.name} can't turn, is not in motion")

    def show_speed(self):
        print(f'Speed = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speeding!")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speeding!")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


t_car = TownCar(60, "red", "Honda", 0)
s_car = SportCar(200, "blue", "Suzuki", 0)
w_car = WorkCar(40, "white", "Lada", 0)
p_car = PoliceCar(80, "green", "Skoda", 1)


t_car.turn("right")
t_car.go()
t_car.turn("right")

w_car.show_speed()
w_car.speed = 100
w_car.show_speed()


p_car.turn("left")
print(bool(p_car.is_police))
p_car.go()
p_car.show_speed()