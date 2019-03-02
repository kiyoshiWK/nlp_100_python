# -*- coding: utf-8 -*-

def make_word_opsition_dict(word_list, position_list):
    result = {}
    for i in range(len(word_list)):
        if i+1 in position_list:
            key = word_list[i][0:1]
            result[key] = i+1
        else:
            key = word_list[i][0:2]
            result[key] = i+1
    return result

def get_word_list(sentence):
    table = sentence.maketrans({
        ',': '',
        '.': ''
    })
    return sentence.translate(table).split(' ')


def main(sentence, position_list):
    word_list = get_word_list(sentence)
    word_position_dict = make_word_opsition_dict(word_list, position_list)
    print(word_position_dict)

if __name__ == '__main__':
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    position_list = [1, 5, 6, 7, 8, 9, 15, 16]
    main(sentence, position_list)