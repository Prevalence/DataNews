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
    stop=['习近平','总书记','指出','更加','重要讲话','着力','作出','强调','广大','各位','不断','不断','文选','这是','一些','特别','不能','这个','就是','人民出版社','这个','一个','没有','就是','他们','不能','可以','这样','一些','但是','这是','不是','自己','如果','一点','有些','什么','能够','关于','当然','特别','不要','这次','对于','比较','所以','可能']
    f=open(name,'r')
    passage=f.read()
    tfidf = jieba.analyse.extract_tags
    keywords = tfidf(passage,topK=number)
    for i in stop:
        if i in keywords:
            keywords.remove(i)
    f.close
    path=name.split('.txt')[0]+'分词版.txt'
    path=path.replace('Corpus','Data2Analyse')
    f=open(path,'r')
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
    print(len(keywords))
#将关键词和频率存入excel
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('book_top250',cell_overwrite_ok=True)
    sheet.write(0,0,'关键词')
    sheet.write(0,1,'调整前频率')
    sheet.write(0,2,'调整后频率')
    sheet.write(0,3,'平均每万词出现的次数')
    for i in range((len(keywords))):
        sheet.write(i+1,0,keywords[i])
        sheet.write(i+1,1,frequency[i])
        sheet.write(i+1,2,frequency[i]*10)
        sheet.write(i+1,3,int(frequency[i]*10000))
    path=path.replace('分词版','')
    workbook.save(path.split('.txt')[0]+'.xls')
    
def findDup():
    f1=open('../Corpus/江泽民讲话.txt','r')
    f2=open('../Corpus/习近平讲话.txt','r')
    f3=open('../Corpus/邓小平讲话.txt','r')
    stop=['习近平','总书记','指出','更加','重要讲话','着力','作出','强调','广大','各位','不断','不断','文选','这是','一些','特别','不能','这个','就是','人民出版社','这个','一个','没有','就是','他们','不能','可以','这样','一些','但是','这是','不是','自己','如果','一点','有些','什么','能够','关于','当然','特别','不要','这次','对于','比较','所以','可能']
    tfidf = jieba.analyse.extract_tags
    p1=f1.read()
    p2=f2.read()
    p3=f3.read()
    k1 = tfidf(p1,topK=100)
    k2=tfidf(p2,topK=100)
    k3=tfidf(p3,topK=100)
    f1.close()
    f2.close()
    f3.close()
    result=[]
    f4=open('../Data2Analyse/重复词.txt','w')
    for i in k1:
        if i in stop:
            continue
        else:
            if i in k2 and i in k3:
                f4.write(i+'\n')
    f4.close()
                
                
    return result

if __name__=='__main__':
    #getWordPiece('Corpus/江泽民讲话.txt')
    getKeywords('../Corpus/邓小平讲话.txt',100)
    #print(findDup())