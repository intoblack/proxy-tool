#coding=gbk


import time
from Crawler import Crawler
from starturl import BaiduSeed 
from ProxyData import ProxySave
from UrlQueue import TaskQueue

TaskQueue.getInstance().put(("http://www.cnproxy.com/proxy6.html",-1))
pt = BaiduSeed(["代理http","免费代理http","代理 http"])
p = ProxySave()
p.start()
for i in range(70):
    c = Crawler(1)
    c.start()
    time.sleep(3)



    
