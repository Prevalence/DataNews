# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 21:17:49 2017

@author: John
"""

import jieba.analyse
import xlwt
#获取分词后版本的讲话文件
def getWordPiece(name):
    f=open(name,'r')
    content=f.read()
    seg_list=list(jieba.cut(content))
    f.close()
    f=open(name.split('.txt')[0]+'分词版.txt','a')
    for i in seg_list:
       if len(i)>1:
           f.write(i)
           f.write('/')
    f.close()

#获得关键词并在分词版文件中统计词频
def getKeywords(name,number):
    f=open(name,'r')
    passage=f.read()
    tfidf = jieba.analyse.extract_tags
    keywords = tfidf(passage,topK=number)
    f.close
    f=open(name.split('.txt')[0]+'分词版.txt','r')
    content=f.read()
    content=content.split('/')
    dict={}
    for i in content:
        if i in dict:
            temp=dict[i]
            temp=temp+1
            dict[i]=temp
        else:
            dict[i]=1
    frequency=[]
    wholeSize=len(content)
    f.close()
    for i in keywords:
        frequency.append(dict[i]/wholeSize)
    print(keywords)
    print(frequency)
#将关键词和频率存入excel
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('book_top250',cell_overwrite_ok=True)
    sheet.write(0,0,'关键词')
    sheet.write(0,1,'调整前频率')
    sheet.write(0,2,'调整后频率')
    for i in range((len(keywords))):
        sheet.write(i+1,0,keywords[i])
        sheet.write(i+1,1,frequency[i])
        sheet.write(i+1,2,frequency[i]*10)
    workbook.save(name.split('.txt')[0]+'.xls')
    
    
    
if __name__=='__main__':
    getWordPiece('Corpus/江泽民讲话.txt')
    getKeywords('Corpus/江泽民讲话.txt',30)