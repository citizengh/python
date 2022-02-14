from functools import reduce
with open("text_3.txt", "r", encoding="UTF-8") as reader:
    lines = reader.readlines()
    print([line.split()[0] for line in lines if float(line.split()[1]) < 20000])
    print(f'Средняя з/п:{round(reduce(lambda a, b: a + b,map(lambda line: float(line.split()[1]), lines)) / len(lines),2) }')

