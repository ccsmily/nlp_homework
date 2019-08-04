# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 
def train_fun(filepath):
    wiki_news = open(filepath, 'r', encoding = 'utf-8')
    model = Word2Vec(LineSentence(wiki_news), sg=0,size=200, window=5, min_count=50, workers=2)
    model.save('./model/wiki_news.word2vec')
 
if __name__ == '__main__':
    train_fun('./merge')