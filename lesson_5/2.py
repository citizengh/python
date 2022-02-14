with open("myFirstFile.txt", "r", encoding="UTF-8") as reader:
    lines = reader.readlines()
    print([f'{lines.index(l) + 1} - {len(l.split())} слов' for l in lines])


