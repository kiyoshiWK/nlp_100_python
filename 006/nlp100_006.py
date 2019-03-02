# -*- coding: utf-8 -*-

import sys

def make_char_ngram_list(sentence, n):
    if n > len(sentence):
        sys.exit('ERROR: "n" is bigger than length of sentence')
    else:
        result = set()
        for i in range(len(sentence) - (n-1)):
            result.add(sentence[i:i+n])
        return result

def get_set_result(type, set_list):
    result = set()
    if type == 'union':
        for i in range(len(set_list)):
            result = result.union(result, set_list[i])
    elif type == 'intersection':
        for i in range(len(set_list)):
            result = result.intersection(result, set_list[i])
    elif type == 'difference':
        for i in range(len(set_list)):
            result = result.difference(result, set_list[i])
    else:
        sys.exit('ERROR: type is not effective. please input type either "union" or "intersection" or "difference')
    return result

def get_2set_result(type, set_01, set_02):
    result = set()
    if type == 'union':
        result = set.union(set_01, set_02)
    elif type == 'intersection':
        result = set.intersection(set_01, set_02)
    elif type == 'difference':
        result = set.difference(set_01, set_02)
    else:
        sys.exit('ERROR: type is not effective. please input type either "union" or "intersection" or "difference')
    return result

def check_contain_target_str(ngram_set, target_str):
    if target_str in ngram_set:
        return True
    else:
        return False

def main(sentence_01, sentence_02, target_str):
    X = make_char_ngram_list(sentence_01, 2)
    Y = make_char_ngram_list(sentence_02, 2)

    set_list = [X, Y]

    # union_set = get_set_result('union', set_list)
    union_set = get_2set_result('union', X, Y)
    print('union: ' + str(union_set))

    # intersection_set = get_set_result('intersection', set_list)
    intersection_set = get_2set_result('intersection', X, Y)
    print('intersection: ' + str(intersection_set))

    # difference_set = get_set_result('difference', set_list)
    difference_set = get_2set_result('difference', X, Y)
    print('difference: '+ str(difference_set))

    print('check_contain_"'+target_str+'"_in_X: ' + str(check_contain_target_str(X, target_str)))
    print('check_contain_"'+target_str+'"_in_Y: ' + str(check_contain_target_str(Y, target_str)))


if __name__ == '__main__':
    sentence_01 = 'paraparaparadise'
    sentence_02 = 'paragraph'
    target_str = 'se'
    main(sentence_01, sentence_02, target_str)