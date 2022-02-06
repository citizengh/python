my_list = []

n = int(input("Введите количество элементов: "))
print("Введите элементы: ")
for i in range(0, n):
    my_list.append(input())

print(my_list)

i = 0
while i < len(my_list)-1:
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2

print(my_list)
