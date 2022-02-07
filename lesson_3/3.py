def my_func(x1, x2, x3):
    try:
        min_num = min(float(x1), float(x2), float(x3))
        return x1+x2+x3-min_num
    except:
        return 0


print(my_func(4,4,4))
print(my_func(15.6,45,0.6))
print(my_func('d',4,'e'))