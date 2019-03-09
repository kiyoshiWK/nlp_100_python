# -*- coding: utf-8 -*-

import os

def extract_category_lines(wikipedia_file_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output:
        with open(wikipedia_file_path, 'r', encoding='utf-8') as read:
            for line in read:
                if 'Category' in line:
                    output.write(line)

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/jawiki-country_england.txt')
    output_file_path = os.path.join(root_path, 'category.txt')

    extract_category_lines(file_path, output_file_path)

if __name__ == '__main__':
    main()