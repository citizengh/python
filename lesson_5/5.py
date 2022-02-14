with open('text_5.txt', "r+", encoding="UTF-8") as writer:
    writer.write('1 2 3 4 5 6 7')
    writer.seek(0)
    print(f'Сумма чисел = {sum(map(float, writer.readline().split()))}')

