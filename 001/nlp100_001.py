# -*- coding: utf-8 -*-

def get_max_position(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    return max

def extract_positioned_str(s, list):
    max_position = get_max_position(list)
    if max_position > len(s):
        return 'error'
    else:
        result = ''
        for i in list:
            result += s[i:i+1]
        return result

def main(str, list):
    result = extract_positioned_str(str,list)
    if result == 'error':
        print('[ERROR]position is out of string')
    else:
        print(result)


if __name__ == '__main__':
    str = 'パタトクカシーー'
    list = [1, 3, 5, 7]
    main(str, list)