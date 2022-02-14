def func_sum_str(my_str):
    retStr = ''
    for s in my_str:
        if s.isdigit():
            retStr += s
        else:
            retStr += " "
    retStr = " ".join(retStr.split())
    return sum(map(int, retStr.split()))


with open('text_6.txt', "r", encoding="UTF-8") as reader:
    lines = reader.readlines()
    d = {line.split(':')[0] : func_sum_str(line.split(':')[1]) for line in lines}
    print(d)


