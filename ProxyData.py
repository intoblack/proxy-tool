#!/usr/bin/env python
#coding=utf-8

import threading
import time
import os
import datetime
from util.ProxyException import NoFilePathException
import util.fileutil as util


class ProxyData(object):
    
    
    __instance = None
    __lock = threading.Lock()  
    __proxydata =  {}
    
    
    def put(self ,  data):
        if isinstance(data, list):
            for proxy in data:
                self.__proxydata[proxy] = 1
        else:
            self.__proxydata[data] = 1
    
    
    def get(self):
        return self.__proxydata.keys()
     
     
    @staticmethod
    def getInstance():
        if not ProxyData.__instance:
            ProxyData.__lock.acquire()
            if not ProxyData.__instance:
                ProxyData.__instance = object.__new__(ProxyData)
                object.__init__(ProxyData.__instance)
            ProxyData.__lock.release()
        return ProxyData.__instance



class ProxySave(threading.Thread):
    
    __saveproxy = {}
    time_format = '%Y-%m-%d-%H-%M-%S'
    savepath = ''
    def __init__(self,savepath , delay  = 10):
        threading.Thread.__init__(self)
        if os.path.isdir(savepath) and os.path.exists(savepath):
            self.savepath = savepath + datetime.datetime.strftime(self.time_format) + '.proxy'
        elif os.path.isfile(savepath):
            self.savepath = savepath
        else:
            raise NoFilePathException,savepath
        if isinstance(delay, int):
            if delay <= 0 :
                self.delay = 10
            self.delay = delay
        else:
            self.delay = delay
            
    
    def save(self,data):
        util.append_write(self.savepath, util.make_contents(data))
    
    def run(self):
        while True:
            time.sleep(self.delay)
            savedata = [val for val in ProxyData.getInstance().get() if val not in self.__saveproxy.keys()]
            if len(savedata) == 0:
                continue
            self.save(savedata)
            
            for proxy in savedata:
                self.__saveproxy[proxy] = 1
            
            


if __name__ == "__main__":
    a = [1 ,2 , 3]
    b = [3 ,4 , 5]
    
    print [val for val in b if val not in a]
            
            