#!/usr/bin/env python
#coding=gbk


import urllib
from urlpool import UrlPool
from UrlQueue import TaskQueue

class BaiduSeed(object):
    
    keyword= []
    
    def __init__(self , keyword = []):
        self.keyword.extend(keyword)
        if not isinstance(keyword, list):
            raise TypeError("KEY_EORD_MUST_BE_LIST")
        for _kw in keyword:
            searchword = self.keyword.pop()
            url = self.baidu_search(searchword)
            if not UrlPool.getInstance().exist(url):
                TaskQueue.getInstance().put((url,-10))
    
    def baidu_search(self,keyword):
        p= {'wd': keyword}
        return "http://www.baidu.com/s?"+urllib.urlencode(p)
       
    
    def get_keyword_url(self , _keyword):
        _url = self.baidu_search(_keyword)
        return _url 

    
    def add_keyword(self,word):
        if isinstance(word, list):
            self.keyword.extend(word)
        else:
            self.keyword.append(word)
    



            
        
