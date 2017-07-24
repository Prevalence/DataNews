# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:17:49 2017

@author: John
"""

import jieba.analyse
f=open('习近平讲话.txt','r')
passage=f.read()
tfidf = jieba.analyse.extract_tags
keywords = tfidf(passage,topK=50)
print(keywords)