my_list = [7, 5, 3, 3, 2]

num = int(input('Введите число:'))

pos = 0

while pos < len(my_list):
    if my_list[pos] <= num:
        break
    else:
        pos += 1

my_list.insert(pos, num)

print(my_list)
