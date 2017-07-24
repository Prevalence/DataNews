# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request
import re
#江泽民文选第一卷的地址为http://cpc.people.com.cn/GB/64184/64185/180137/10818669.html到http://cpc.people.com.cn/GB/64184/64185/180137/10818749.html
#第二卷的地址为"http://cpc.people.com.cn/GB/64184/64185/180138/10818623.html"到http://cpc.people.com.cn/GB/64184/64185/180138/10821826.html
def getXiPassage():
    parenturl='http://china.newssc.org/system/topic/2335/index_zyjh.shtml'
    parentcontent = urllib.request.urlopen(parenturl,timeout=3).read()
    urls=re.findall( r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", parentcontent.decode('gb2312','ignore'),re.I|re.S|re.M)
    f=open('习近平讲话.txt','a')
    for i in urls:
        if 'china.newssc' in i and not('topic' in i):
            data=urllib.request.urlopen(i,timeout=3).read()
            passage=data.decode('gb2312','ignore')
            passage=re.findall(r'<p( style="TEXT-INDENT: 2em")?>(.*?)</p>',passage,re.I|re.S|re.M)
            for j in passage:
                if len(j)>1:
                    j=j[1]
                j=j.replace('<strong>',"")
                j=j.replace('</strong>',"")
                print(j)
                for k in j:
                    try:
                        f.write(k)
                    except Exception as err:
                        continue;
    f.close()
    


def getJiangPassage():
    url="http://cpc.people.com.cn/GB/64184/64185/180137/10818669.html"
    for i in range(523,650):
        try:
            url="http://cpc.people.com.cn/GB/64184/64185/180139/10818"+str(i)+".html"
            print('----------doing'+url+'-------------')
            data = urllib.request.urlopen(url,timeout=3).read()
            data = data.decode('GB2312','ignore')
            passage=data.split('<font id="zoom">')[1]
            passage=passage.split('</font>')[0]
            passage=passage.replace('<P>','')
            passage=passage.replace('</P>','')
            passage=passage.replace("<BR>","")
            passage=passage.replace("</BR>","")
            passage=passage.replace("<br>","")
            passage=passage.replace("</br>","")
            passage=passage.replace("<STRONG>","")
            passage=passage.replace("</STRONG>","")
            passage=passage.replace("&nbsp","")
            #此处passage已经爬取完成，考虑将爬取文件名和网页标题名关联起来
            f=open('江泽民讲话.txt','a')
            for i in passage:
                try:
                    f.write(i)
                except Exception as err:
                    continue;
            f.close()
        except Exception as err:  
            print(url)

if __name__=='__main__':
    getXiPassage();