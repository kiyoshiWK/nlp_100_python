# -*- coding: utf-8 -*-

import os

def merge_col_files(file_path_col1, file_path_col2, output_file_path, delimiter):
    with open(output_file_path, 'w', encoding='utf-8') as output:

        col_data_list = []

        index = 0

        with open(file_path_col1, 'r', encoding='utf-8') as read:
            for line in read:
                line = line.strip('\r\n')
                col_data_list.append({'col1': line})
                index += 1

        index = 0
        with open(file_path_col2, 'r', encoding='utf-8') as read:
            for line in read:
                line = line.strip('\r\n')
                col_data = col_data_list[index]
                col_data['col2'] = line
                index += 1

        for i in range(len(col_data_list)):
            col_data = col_data_list[i]
            output.write(delimiter.join([
                col_data['col1']
                , col_data['col2']
            ]) + '\n')

def main():
    root_path = os.getcwd()
    file_path_col1 = os.path.join(root_path, '../file/col1.txt')
    file_path_col2 = os.path.join(root_path, '../file/col2.txt')
    output_file_path = os.path.join(root_path, 'merge_col_files.txt')

    merge_col_files(file_path_col1, file_path_col2, output_file_path, '\t')

if __name__ == '__main__':
    main()