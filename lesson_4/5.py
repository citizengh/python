from functools import reduce
mult = reduce(lambda x, y: x * y, [num for num in range(100, 1001, 2)])
print(mult)
