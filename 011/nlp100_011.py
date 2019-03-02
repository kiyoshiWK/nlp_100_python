# -*- coding: utf-8 -*-

import os

def output_cooverted_file(read_file_path, output_file_path, prev, after):
    with open(output_file_path, 'w', encoding='utf-8') as output:
        with open(read_file_path, 'r', encoding='utf-8') as read:
            for line in read:
                output.write(line.replace(prev, after))

def main():
    root_path = os.getcwd()
    read_file_path = os.path.join(root_path, '../file/hightemp.txt')
    output_file_path = os.path.join(root_path, 'converted_hightemp.txt')

    output_cooverted_file(read_file_path, output_file_path, '\t', ' ')

if __name__ == '__main__':
    main()