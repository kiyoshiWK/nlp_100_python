# -*- coding: utf-8 -*-

import os

def extract_col_n(file_path, output_path, n):
    with open(output_path, 'w', encoding='utf-8') as output:
        with open(file_path, 'r', encoding='utf-8') as read:
            for line in read:
                line = line.strip('\r\n')
                split = line.split('\t')
                if len(split) >= n:
                    output.write(split[n-1] + '\n')

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/hightemp.txt')
    output_path_col1 = os.path.join(root_path, '../file/col1.txt')
    output_path_col2 = os.path.join(root_path, '../file/col2.txt')

    extract_col_n(file_path, output_path_col1, 1)
    extract_col_n(file_path, output_path_col2, 2)

if __name__ == '__main__':
    main()