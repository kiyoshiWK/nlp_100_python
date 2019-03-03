# -*- coding: utf-8 -*-

import sys
import os

def count_file_line(file_path):
    line_num = 0
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            line_num += 1
    return line_num

def get_split_line_num(line_num, split_num):
    mod = line_num % split_num
    if mod == 0:
        return line_num // split_num
    else:
        return line_num // split_num + 1

def split_file(file_path, split_num, root_path, output_file_name_prefix):
    line_num = count_file_line(file_path)
    split_line_num = get_split_line_num(line_num, split_num)
    line_count = 0
    file_count = 1
    output_file_path = os.path.join(root_path, output_file_name_prefix + str(file_count) + '.txt')
    output = open(output_file_path, 'w', encoding='utf-8')
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            output.write(line)
            line_count += 1
            if line_count % split_line_num == 0:
                output.close()
                file_count += 1
                output_file_path = os.path.join(root_path, output_file_name_prefix + str(file_count) + '.txt')
                output = open(output_file_path, 'w', encoding='utf-8')
                continue
    output.close()

def main():
    if len(sys.argv) < 2:
        print('[ERROR] please input file split num')
        sys.exit()

    split_num = int(sys.argv[1])
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/hightemp.txt')
    output_file_name_prefix = 'split_hightemp_'

    split_file(file_path, split_num, root_path, output_file_name_prefix)

if __name__ == '__main__':
    main()