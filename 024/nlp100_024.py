# -*- coding: utf-8 -*-

import os

def extract_media_file_names(file_path, output_path):
    with open(output_path, 'w', encoding='utf-8') as output:
        with open(file_path, 'r', encoding='utf-8') as read:
            for line in read:
                line = line.strip('\r\n')
                if 'File:' in line:
                    media_file_name = line.split('File:')[1].split('|')[0]
                    output.write(media_file_name + '\n')
                elif 'ファイル:' in line:
                    media_file_name = line.split('ファイル:')[1].split('|')[0]
                    output.write(media_file_name + '\n')

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/jawiki-country_england.txt')
    output_file_path = os.path.join(root_path, 'media_file_name.txt')

    extract_media_file_names(file_path, output_file_path)

if __name__ == '__main__':
    main()