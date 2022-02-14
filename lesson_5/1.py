with open("myFirstFile.txt", "w", encoding="UTF-8") as writer:
    while True:
        userInput = input("Введите данные:")
        if userInput == '':
            break
        writer.write(f'{userInput}\n')