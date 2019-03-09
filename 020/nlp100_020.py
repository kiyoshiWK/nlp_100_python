# -*- coding: utf-8 -*-

import os
import json

def make_wikipedia_data_dict(json_file_path):
    f = open(json_file_path, 'r', encoding='utf-8')
    wikipedia_data_dict = json.load(f)

    return wikipedia_data_dict

def extract_article_text(wikipedia_data_dict, title, output_file_path):
    wikipedia_data_list = wikipedia_data_dict['wikipedia_data']
    with open(output_file_path, 'w', encoding='utf-8') as output:
        for i in range(len(wikipedia_data_list)):
            if title in wikipedia_data_list[i]['title']:
                output.write(wikipedia_data_list[i]['text'])

def main():
    root_path = os.getcwd()
    file_path = os.path.join(root_path, '../file/shaped_jawiki-country.json')
    output_file_path = os.path.join(root_path, '../file/jawiki-country_england.txt')

    wikipedia_data_dict = make_wikipedia_data_dict(file_path)

    extract_article_text(wikipedia_data_dict, 'イギリス', output_file_path)

if __name__ == '__main__':
    main()