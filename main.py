#coding=gbk

from Crawler import Crawler
import time
from ProxySpider import BaiduSeed 
from ProxyData import ProxySave
from UrlQueue import TaskQueue

TaskQueue.getInstance().put(("http://www.cnproxy.com/proxy6.html",-1))
pt = BaiduSeed(["����http","��Ѵ���http","���� http"])
p = ProxySave()
p.start()
for i in range(70):
    c = Crawler(1)
    c.start()
    time.sleep(3)



    
