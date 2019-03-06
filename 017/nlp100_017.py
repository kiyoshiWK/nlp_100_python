# -*- coding; utf-8 -*-

import os

def make_first_char_set(file_path):
    first_char_set = set()
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            first_char = line[:1]
            first_char_set.add(first_char)
    return first_char_set

def main():
    root_path = os.getcwd()
    input_file_path = os.path.join(root_path, '../file/hightemp.txt')

    first_char_set = make_first_char_set(input_file_path)

    print('num of different char is ' + str(len(first_char_set)))
    print(first_char_set)

if __name__ == '__main__':
    main()