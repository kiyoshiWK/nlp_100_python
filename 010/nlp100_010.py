# -*- coding: utf-8 -*-

import os

def count_line_num(file_path):
    line_num = 0
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            line_num += 1
    return line_num

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/hightemp.txt')
    print('line num is ' + str(count_line_num(file_path)))

if __name__ == '__main__':
    main()