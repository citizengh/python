month = int(input('Введите месяц(1-12):'))
if month < 1 or month > 12:
    print('Ошибка ввода данных!')
    exit(0)
list_seasons = ['Зима', 'Весна', 'Лето', 'Осень']
print(list_seasons[((month % 12) // 3)])

my_dict = {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12:0}
print(list_seasons[my_dict[month]])