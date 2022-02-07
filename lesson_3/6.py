def word_func(my_word):
    '''Возвращает строку с заглавной буквы'''
    word = ''
    for l in my_word:
        if 91 < ord(l) < 123:
            word += l
        else:
            return ''
    return word.title()


print(word_func(input('Введите слово:')))


def sent_func(my_sentence):
    '''Возвращает слова с заглавной буквы'''
    sentence = ''
    my_sentence = " ".join(my_sentence.split())
    my_sentence = my_sentence.split(' ')
    for word in my_sentence:
        sentence += word_func(word) + ' '
    sentence = " ".join(sentence.split())
    return sentence


print(sent_func(input('Введите предложение:')))
