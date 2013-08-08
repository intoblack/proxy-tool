'''
Created on 2013-6-26

@author: lixuze
'''
from Queue import LifoQueue
import threading


class UrlPool(object):
    '''
    classdocs
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
            
class mqueue(LifoQueue):
    def _put(self, item):
        if isinstance(item, list):
            self.queue.extend(item)
        else:
            self.queue.append(item)
            

        
        


    
        