def neg_power(num, degree):
    '''num - действительное число, degree - отрицательное целое'''
    try:
        float(num)
        int(degree)
        if int(degree) >= 0:
            raise ValueError()
    except ValueError:
        return 'Некорректное значение аргумента!'

    degree += 1
    result = num

    while degree < 0:
        result *= num
        degree += 1

    return (round((1 / result), 5))


print(neg_power(2,0))
print(neg_power(4,-2))
print(neg_power(4,-1))
print(neg_power(4,1))
print(neg_power(10, -2))
