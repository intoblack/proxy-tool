#coding=utf8
import threading
from urlpool import mqueue

class TaskQueue(object):
    
    
    WALK_URL_LIST = mqueue(10000)
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