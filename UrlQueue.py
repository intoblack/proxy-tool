#coding=utf8

import threading
from Queue import LifoQueue


class UrlPool(object):
    '''

    '''
    URL_DICT = {}
    __instance = None
    __lock = threading.Lock()    

    
    @staticmethod
    def getInstance():
        if not UrlPool.__instance:
            UrlPool.__lock.acquire()
            if not UrlPool.__instance:
                UrlPool.__instance = object.__new__(UrlPool)
                object.__init__(UrlPool.__instance)
            UrlPool.__lock.release()
        return UrlPool.__instance
    
    def exist(self , url):
        if self.URL_DICT.has_key(url):
            return True
        return False
    
    
    def put_url(self , url):
        
        if not self.URL_DICT.has_key(url):
            self.URL_DICT[url] = 1
    
    def print_all_url(self):
        for _key , _val in self.URL_DICT.items():
            print '%s\t\t%s' % (_key,_val)
    
    
    
    def __str__(self, *args, **kwargs):
        '''
        print 函数
        '''
        msg = []
        for _key , _val in self.URL_DICT.items():
            msg.append('%s\t\t%s')
        return '\n'.join(msg)
            
class MQueue(LifoQueue):
    
    def _put(self, item):
        if isinstance(item, list):
            self.queue.extend(item)
        else:
            self.queue.append(item)
            
            
            
class TaskQueue(object):
    
    
    WALK_URL_LIST = MQueue(10000)
    __instance = None
    __lock = threading.Lock()      
    
    
    @staticmethod
    def getInstance():
        if not TaskQueue.__instance:
            TaskQueue.__lock.acquire()
            if not TaskQueue.__instance:
                TaskQueue.__instance = object.__new__(TaskQueue)
                object.__init__(TaskQueue.__instance)
            TaskQueue.__lock.release()
        return TaskQueue.__instance
    
    def get(self):
        url = None
        self.__lock.acquire()
        if not self.WALK_URL_LIST.empty():
            url = self.WALK_URL_LIST._get()
        self.__lock.release()
        return url
    
    def put(self, url):
        self.WALK_URL_LIST._put(url)
    
    def isempty(self):
        return self.WALK_URL_LIST.empty()