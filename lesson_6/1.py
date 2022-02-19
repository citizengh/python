import time


class TrafficLight:
    _color = ""

    def running(self):
        program = {"Red": 7, "Yellow": 2, "Green": 5}
        for pair in program:
            _color = pair
            print(_color)
            time.sleep(program[pair])


t = TrafficLight()
t.running()
