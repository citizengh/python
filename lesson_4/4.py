my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#способ 1
print([num for num in my_list if my_list.count(num) == 1])

#способ 2
my_dict = {num: my_list.count(num) for num in my_list}
print([key for key in my_dict.keys() if my_dict[key] == 1])
