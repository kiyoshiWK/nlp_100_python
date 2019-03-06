# -*- coding: utf-8 -*-

import os

def make_dic(file_path):
    result = {}
    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            split = line.strip('\r\n').split('\t')
            key = split[2]
            value = line.strip('\r\n')
            result[key] = value
    return result

def main():
    root_path = os.getcwd()
    input_file_path = os.path.join(root_path, '../file/hightemp.txt')

    data_dic = make_dic(input_file_path)

    for k, v in sorted(data_dic.items(), reverse=True):
        print(v)

if __name__ == '__main__':
    main()