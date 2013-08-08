#!/usr/bin/env python
#coding=utf-8

import threading
from ProxyTest import open_url
from   UrlQueue import TaskQueue
from ProxyData import ProxyData
import time

class AssertProxy(threading.Thread):
    
    
    def __init__(self):
        threading.Thread.__init__(self)
    
    
    
    def run(self):
        while not TaskQueue.getInstance().isempty():
            print "run"
            task = TaskQueue.getInstance().get()
            sign = True
            time.sleep(2)
            for i in range(1):
                taskarry = task.split(":")
                print task
                if len(taskarry) == 2:
                    if not open_url('http://open.weibo.com/',taskarry[0],taskarry[1],"新浪微博",2):
                        sign = False
            if sign:
                ProxyData.getInstance().put(task)

                
                
    
    
    


