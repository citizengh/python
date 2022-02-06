my_list = [2, 'text', True, 45.3, [1, 2, 3]]
print(my_list)
for i in my_list:
    print(f"{str(i):>9}" + f",тип : {type(i)}")
