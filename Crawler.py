#!/usr/bin/env python
# -*- coding: gbk -*-

import urllib2
from urlpool import UrlPool 
from UrlQueue import TaskQueue
from BeautifulSoup import BeautifulSoup
import re
import threading
from ProxyData import ProxyData
import time


class Crawler(threading.Thread):
    proxyregx = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(<SCRIPT type=text/javascript>document.write\(\":\"(\+[a-z]?)+\)</SCRIPT>|:[0-9]{1,}){1}")
    alive = True


    def __init__(self , level = 1 , retrycount = 300 ):
        threading.Thread.__init__(self)
        self.level = level
        self.initempty = retrycount
        self.emptycount = retrycount
    
    def downloadhtml(self, url , timeout=5 , coding = 'gbk'):
        html = urllib2.urlopen(url=url , timeout = timeout).read().decode(coding, 'ignore')
        return html
    

    def proxy_parser(self , html):
        proxylist = []
        for m in self.proxyregx.finditer(html):
            proxylist.append(m.group())
        return proxylist
    

    
    def get_link(self,html , level , rooturl):
        '''
        '''
        soup = BeautifulSoup(html)
        linklist = []
        for link in soup.findAll('a'):
            link = link.get("href")
            if link:
                linklist.append((self.make_absolute_url(rooturl,link),level))
        return linklist
    
    def make_absolute_url(self,base_url, relative_url):
        from urlparse import urlparse, urljoin
        url = urlparse(relative_url)
        if url.scheme == url.netloc == "":
            return urljoin(base_url, relative_url)
        else:
            return relative_url


    def run(self):
        while self.alive:
            time.sleep(1)
            walk_url = TaskQueue.getInstance().get()
            if not walk_url:
                self.emptycount = self.emptycount - 1
                if self.emptycount == 0 :
                    return
                continue
            self.emptycount = self.initempty
            _level = walk_url[1]
            _url = walk_url[0]
            if _level > self.level:
                continue 
            if UrlPool.getInstance().exist(_url):
                continue
            UrlPool.getInstance().put_url(_url)
            try:
                html = self.downloadhtml(_url,coding="gb2312")
            except Exception,e:
                print e
                continue   
            proxydata = self.proxy_parser(html)
            _level = _level + 1 
            if len(proxydata):
                ProxyData.getInstance().put(proxydata)
                _level = 0 
            link_list = self.get_link(html,_level,_url)
            for  link in link_list:
                if not UrlPool.getInstance().exist(link[0]):
                    TaskQueue.getInstance().put(link)
                                  
            
if __name__ == "__main__":
    TaskQueue.getInstance().put(("http://www.baidu.com/s?wd=%E5%85%8D%E8%B4%B9%E4%BB%A3%E7%90%86",0))
    c = Crawler(2)
    c.start()     
#     print urllib2.urlopen('http://www.baidu.com/baidu.php?url=VxDK00K9of64oISQpyg_IgzoBHhHdMD6WtbN1AsJGsxhoGCHL4BzXAEnrlC5V0PAJzIcsLPsQGe4LTmMA9pW-6NvbIAJKhLEPR-LjpI5BWEtYYSlLZSRScWGYgGMNm-Ca8o2khn.DD_iRnE-bvces8YGSOzmLUQ2ld2s1f_N4rrzkf.U1Yk0ZDqsS2LYUHlsrY0IjLj3oxwV5o0efKGUHYznWT0u1dsTvwYn0KdpHdBmy-bIfKspyfqnHb0mv-b5HRd0AdY5HDsnHIxnH0knsKopHYs0ZFY5iYk0ANGujY1nj6Yg1DYPjuxnWT3PNt1njR4g1c4rj7xn104n7tznWf4g1c4P1KxnWRYndtzrHfzg1cLnjc0mhbqrj6Yr0KVm1Y1n10YPjbYnNtkPWc1P1fLnfKkTA-b5H00TyPGujYs0ZFMIA7M5H00ULu_5fK9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KzpWYs0Aw-IWdsmsKBUjYs0APzm1Y1P1fznf').read() 