from itertools import count
from itertools import cycle

##### 1
start_num = 3
stop_num = 27

iterator = count(start_num, 1)

while start_num < stop_num:
    start_num = next(iterator)
    print(start_num)


##### 2
my_list = ['red', 'yellow', 'green']

iter = cycle(my_list)
stop = 100
current = 0
while current < stop:
    print(next(iter))
    current += 1

