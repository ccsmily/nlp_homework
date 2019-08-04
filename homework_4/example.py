# -*- coding: utf-8 -*-
import gensim
import logging
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
model = gensim.models.Word2Vec.load('./model/wiki_news.word2vec')
   
def test():
    result = model.most_similar('人工智能',topn=10)
    print(result)
    res = model.similarity('腾讯', '阿里巴巴')
    print("similarity:%.4f"%res)

def visualization():
    labels = []
    tokens = list(range(len(model.wv.vocab)))
    print(len(model.wv.vocab))
    for (i, word) in enumerate(model.wv.vocab):
        tokens[i] = model[word]
        labels.append(word)    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)
    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        if i%100: print(i)
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

if __name__ == '__main__':
    test()
    visualization()