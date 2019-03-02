# -*- coding: utf-8 -*-

def array_word_length(sentence):
    table = sentence.maketrans({
        ',':'',
        '.':''
    })
    split = sentence.translate(table).split(' ')
    result = ''
    for word in split:
        result += str(len(word))
    return result

def main(sentence):
    print(array_word_length(sentence))

if __name__ == '__main__':
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    main(sentence)