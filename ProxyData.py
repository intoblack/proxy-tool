#!/usr/bin/env python
#coding=utf-8

import threading
import time

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
    def __init__(self,savepath):
        threading.Thread.__init__(self)
        self.savepath = savepath
        self.failcount = 100
    
    def save(self,data):
        filehandle = open(self.savepath , 'a')
        for line in data:
            filehandle.write(line+"\n")
        filehandle.close()
    
    def run(self):
        while True:
            time.sleep(10)
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
            
            