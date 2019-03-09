# -*- coding: utf-8 -*-

import os

def shape_file(wikipedia_file_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output:
        output.write('{"wikipedia_data":[')
        with open(wikipedia_file_path, 'r', encoding='utf-8') as read:
            output.write(read.readline())
            for line in read:
                output.write(''.join([',', line]))
            output.write(']}')

def main():
    root_path = os.getcwd()
    wikipedia_file_path = os.path.join(root_path, '../file/jawiki-country.json')
    shaped_file_path = os.path.join(root_path, '../file/shaped_jawiki-country.json')

    shape_file(wikipedia_file_path, shaped_file_path)

if __name__ == '__main__':
    main()