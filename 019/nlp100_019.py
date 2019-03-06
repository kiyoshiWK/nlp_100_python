# -*- coding: utf-8 -*-

import os

def make_first_char_count_dict(file_path):
    first_char_count_dic = {}
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            first_char = line[:1]
            count = 0
            if first_char in first_char_count_dic.keys():
                count = first_char_count_dic[first_char]
            count += 1
            first_char_count_dic[first_char] = count
    return first_char_count_dic

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/hightemp.txt')

    first_char_count_dic = make_first_char_count_dict(file_path)

    for k, v in sorted(first_char_count_dic.items(), key=lambda x:-x[1]):
        print(str(k) + ':' + str(v))

if __name__ == '__main__':
    main()