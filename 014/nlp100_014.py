# -*- coding: utf-8 -*-

import sys
import os

def count_file_lines(file_path):
    line_num = 0
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            line_num += 1
    return line_num

def print_top_n_lines(file_path, n):
    line_num = count_file_lines(file_path)
    if int(n) > line_num:
        print('[ERROR] your input line num is bigger than file line num.')
        print('[INFO] file line num is "'+ str(line_num) + '"')
        sys.exit()
    with open(file_path, 'r', encoding='utf-8') as read:
        index = 0
        while index <= int(n):
            for line in read:
                print(line)
                index += 1

def main():
    if len(sys.argv) < 2:
        print('[ERROR] please input extract line num')
        sys.exit()
    root_path = os.getcwd()
    extract_line_num = sys.argv[1]
    file_path = os.path.join(root_path, '../file/hightemp.txt')

    print_top_n_lines(file_path, extract_line_num)


if __name__ == '__main__':
    main()