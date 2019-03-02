# -*- coding: utf-8 -*-

import random

def random_arrange(word):
    if len(word) <= 4:
        return word
    else:
        top = word[0:1]
        bottom = word[len(word)-2:len(word)-1]
        char_list = []
        for i in range(len(word)-2):
            char_list.append(word[i+1:i+2])
        random_char_list = random.shuffle(char_list)
        middle = ''.join(char_list)
        return top+middle+bottom


def main(sentence):
    word_list = sentence.split(' ')
    result_list = []
    for word in word_list:
        result_list.append(random_arrange(word))
    print(' '.join(result_list))

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    main(sentence)