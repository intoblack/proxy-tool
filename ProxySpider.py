#!/usr/bin/env python
#coding=gbk


import threading 
import urllib
import re
import time
from urlpool import UrlPool
from UrlQueue import TaskQueue

class ProxySpider(threading.Thread):
    
    keyword= []
    proxyregx = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]+")
    
    def __init__(self , keyword = []):
        threading.Thread.__init__(self)
        self.keyword.extend(keyword)
        self.isalive = True
    
    def baidu_search(self,keyword):
        p= {'wd': keyword}
        return "http://www.baidu.com/s?"+urllib.urlencode(p)
       
    
    def proxy_parser(self , html):
        proxylist = []
        for m in self.proxyregx.finditer(html):
            proxylist.append(m.group())
        return proxylist
    
    def add_keyword(self,word):
        if isinstance(word, list):
            self.keyword.extend(word)
        else:
            self.keyword.append(word)
    
    def set_alive(self,isAlive):
        self.isalive = isAlive
        
    def run(self):
        while self.isalive:
            if len(self.keyword):
                searchword = self.keyword.pop()
                url = self.baidu_search(searchword)
                if not UrlPool.getInstance().exist(url):
                    TaskQueue.getInstance().put((url,-10))
#                 ProxyData.getInstance().put(self.proxy_parser(html))
            time.sleep(1)



if __name__ == "__main__":
    pt = ProxySpider(["免费代理" , "免费http" , "免费http代理"])
    pt.start()
            
            
        
