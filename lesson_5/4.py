my_dict = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
with open("text_4.txt", "r", encoding="UTF-8") as reader:
    with open("text_4_RU.txt", "w", encoding="UTF-8") as writer:
        lines = reader.readlines()
        for line in lines:
            writer.write(f'{my_dict[int(line.split()[2])]} {line.split()[1]} {line.split()[2]} \n')