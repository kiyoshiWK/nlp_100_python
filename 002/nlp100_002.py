# -*- coding: utf-8 -*-

def mutually_connect(str_01, str_02):
    result = ''
    if len(str_01) == len(str_02):
        for i in range(len(str_01)):
            result += str_01[i:i+1] + str_02[i:i+1]
    elif len(str_01) > len(str_02):
        for i in range(len(str_02)):
            result += str_01[i:i+1] + str_02[i:i+1]
        result += str_01[len(str_02):len(str_01)]
    elif len(str_01) < len(str_02):
        for i in range(len(str_01)):
            result += str_01[i:i+1] + str_02[i:i+1]
        result += str_02[len(str_01):len(str_02)]
    return result

def main(str_01, str_02):
    result = mutually_connect(str_01, str_02)
    print(result)

if __name__ == '__main__':
    str_01 = 'パトカー'
    str_02 = 'タクシー'
    main(str_01, str_02)