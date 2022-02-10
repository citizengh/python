def fact(n):
    start = 1
    fact = 1
    for start in range(n):
        yield fact
        start = start + 1
        fact = fact * start


for el in fact(10):
    print(el)
