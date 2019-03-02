# -*- coding; utf-8 -*-

import sys
import os

def count_file_line(file_path):
    line_num = 0
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            line_num += 1
    return line_num

def print_bottom_n_lines(file_path, n):
    line_num = count_file_line(file_path)
    if n > line_num:
        print('[ERROR] your input num is bigger than file line num')
        print('[INFO] file line num is "' + str(line_num) + '"')
        sys.exit()
    with open(file_path, 'r', encoding='utf-8') as read:
        read_line_num = 0
        for line in read:
            read_line_num += 1
            if line_num - n <= read_line_num:
                print(line)

def main():
    if len(sys.argv) < 2:
        print('[ERROR] please input print line num')
        sys.exit()
    line_num = int(sys.argv[1])
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/hightemp.txt')

    print_bottom_n_lines(file_path, line_num)

if __name__ == '__main__':
    main()