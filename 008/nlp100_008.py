# -*- coding: utf-8 -*-

def cipher(string):
    result = ''
    for i in range(len(string)):
        char = string[i:i+1]
        if char.isalpha() and char.islower():
            result += chr(219-ord(char))
        else:
            result += char
    return result

def main(string):
    crypted_string = cipher(string)
    print('before crypt: ' + string)
    print('after crypt : ' + crypted_string)

if __name__ == '__main__':
    string = 'testテスト12345てすと試験'
    main(string)