# -*- coding: utf-8 -*-
import os

def merge(dirpath, output_path):
    output = open(output_path, 'w', encoding = 'utf-8')
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            filepath = root + '/' + filename
            filepath = filepath.replace('\\', '/')
            print(filepath)
            file = open(filepath, 'r', encoding = 'utf-8')
            line = file.readline()
            while line:
                output.writelines(line)
                line = file.readline()
            file.close()
    output.close()
    
if __name__ == '__main__':
    merge('./wiki_zh_jieba', './merge')