# -*- coding: utf-8 -*-

import os
import re

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/tab_test.txt')

    with open(file_path, 'r', encoding='utf-8') as read:
        for line in read:
            if '    ' in line:
                print('find tab')

if __name__ == '__main__':
    main()