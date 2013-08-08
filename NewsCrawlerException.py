'''
Created on 2013-6-26

@author: lixuze
'''

class MyClass(Exception):
    '''
    classdocs
    '''
    
    def __init__(self, reason):
        self.reason = reason.encode('utf-8')

    def __str__(self):
        return self.reason
        