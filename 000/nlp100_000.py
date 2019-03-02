# -*- coding: utf-8 -*-

def get_reverse_string(s):
    result = ''
    for i in range(len(s)):
        result += s[len(s)-i-1:len(s)-i]
    return result

def main():
    str = 'stressed'
    print(get_reverse_string(str))

if __name__ == '__main__':
    main()