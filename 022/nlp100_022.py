#-*- coding; utf-8 -*-

import os

def get_category_name(line):
    line = line.strip('\r\n[]')
    return line.split('Category:')[1]

def extract_category_name(wikipedia_file_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output:
        with open(wikipedia_file_path, 'r', encoding='utf-8') as read:
            for line in read:
                if 'Category' in line:
                    category_name = get_category_name(line)
                    output.write(category_name + '\n')

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/jawiki-country_england.txt')
    output_file_path = os.path.join(root_path, 'category_name.txt')

    extract_category_name(file_path, output_file_path)

if __name__ == '__main__':
    main()