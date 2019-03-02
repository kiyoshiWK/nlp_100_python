# -*- coding: utf-8 -*-
import sys

def make_word_ngram(word_list, n):
    if n > len(word_list):
        sys.exit('ERROR: "n" is bigger than length of word list')
    else:
        result = []
        for i in range(len(word_list)-(n-1)):
            result.append(word_list[i]+word_list[i+1])
        return result

def make_char_ngram(sentence, n):
    table = sentence.maketrans({
        ',':'',
        '.':'',
        ' ':''
    })
    sentence = sentence.translate(table)
    if n > len(sentence):
        sys.exit('ERROR: "n" is bigger than length of sentence')
    else:
        result = []
        for i in range(len(sentence)-(n-1)):
            result.append(sentence[i:i+n])
        return result

def get_word_list(sentence):
    table = sentence.maketrans({
        ',': '',
        '.': ''
    })
    return sentence.translate(table).split(' ')

def main(sentence):
    word_list = get_word_list(sentence)
    print('word_list:' + str(word_list))
    word_bigram_list = make_word_ngram(word_list, 2)
    print('word_bigram:' + str(word_bigram_list))

    char_bigram_list = make_char_ngram(sentence, 2)
    print('char_bigram:' + str(char_bigram_list))

if __name__ == '__main__':
    sentence = 'I am an NLPer'
    main(sentence)