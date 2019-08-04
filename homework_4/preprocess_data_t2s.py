# -*- coding: utf-8 -*-
import os

def transfer_tw2s(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            filepath = root + '/' + filename
            filepath = filepath.replace('\\', '/')
            outpath = filepath.replace('wiki_zh', 'wiki_zh_s')
            print(filepath, outpath)
            os.system('opencc -i ' + filepath + ' -o ' + outpath + ' -c opencc-1.0.4-win32/opencc-1.0.4/share/opencc/t2s.json')

if __name__ == '__main__':
    transfer_tw2s('./wiki_zh')