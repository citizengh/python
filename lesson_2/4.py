message = input('Введите предложение:')

words = message.split(' ')

for word in words:
    print(f'{words.index(word)+1}. {word[0:10] }')
