# -*- coding: utf-8 -*-
import os, re, jieba

def jieba_cut_wiki(dirpath):
    for root, dirs, files in os.walk(dirpath):
        for filename in files:
            filepath = root + '/' + filename
            filepath = filepath.replace('\\', '/')
            outpath = filepath.replace('wiki_zh_s', 'wiki_zh_jieba')
            print(filepath)          
            parse_wiki(filepath, outpath)

def stop_word(stop_word_path):
    stop_word_set = set()
    with open(stop_word_path, 'r', encoding = 'utf-8') as stopwords:
        for word in stopwords:
            stop_word_set.add(word.strip('\n'))
    return stop_word_set

def parse_wiki(input_file, output_file):
    file = open(input_file, 'r', encoding = 'utf-8')
    output = open(output_file, 'w+', encoding = 'utf-8')
    regex_str = "[^<doc.*>$]|[^</doc>$]"
    content_line = file.readline()
    article_contents = ''
    stopwords = stop_word('./stopwords.txt')
    while content_line:
        content_line = content_line.strip('\n')
        if len(content_line):
            if re.match(regex_str,content_line):
                words = jieba.cut(content_line, cut_all = False)
                for word in words:
                    if word not in stopwords:
                        article_contents += word + ' '
        else:
            if len(article_contents) > 0:
                output.write(article_contents + '\n')
                article_contents = ''
        content_line = file.readline()
    output.close()
    
if __name__ == '__main__':
    jieba_cut_wiki('./wiki_zh_s')
