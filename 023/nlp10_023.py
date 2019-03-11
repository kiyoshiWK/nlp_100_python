# -*- coding: utf-8 -*-

import os

def extract_section_info(file_path, output_file_path):
    section_level = 1
    with open(output_file_path, 'w', encoding='utf-8') as output:
        output.write(','.join(['section level', 'section name']) + '\n')
        with open(file_path, 'r', encoding='utf-8') as read:
            for line in read:
                line = line.strip('\r\n')
                if line.startswith('===') and line.endswith('==='):
                    section_name = line.strip('===').strip(' ')
                    output.write(','.join([str(section_level), section_name]) + '\n')
                    section_level += 1

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/jawiki-country_england.txt')
    output_file_path = os.path.join(root_path, 'section_name.csv')

    extract_section_info(file_path, output_file_path)


if __name__ == '__main__':
    main()