# -*- coding: utf-8 -*-

import sys

def template(args_list):
    if len(args_list) != 3:
        sys.exit('ERROR: num of args is not 3. please set 3 args.')
    else:
        return str(args_list[0]) + '時の' + str(args_list[1]) + 'は' + str(args_list[2])

def main(args_list):
    print(template(args_list))

if __name__ == '__main__':
    args_list = []
    args_list.append(12)
    args_list.append('気温')
    args_list.append(22.4)

    main(args_list)