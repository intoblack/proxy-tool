#coding=utf-8
#!/usr/bin/env python

import os


class NoFilePathORNotExist(Exception):
    pass

class NoOpinionName(Exception):
    pass

class opinion(dict):
    pass

class comment():
    
    def __init__(self , comment):
        self.comment = comment
        
    def __str__(self):
        return self.comment
        

class Section():
    __data = {}
    __name = ''
    
    
    def get_sections(self):
        return self.__name
    
    def get_opinion(self , key):
        if self.__data.has_key(key):
            return self.__data['key']
        else:
            raise NoOpinionName,key
    
            
    


class Config(object):
    
    __path = None
    __content = []
    __config = {}
    __load = False
    
    
    def __init__(self , filepath ,comment = '#' , config_split = '='):
        if not (filepath and os.path.exists(filepath) and os.path.isfile(filepath)):
            raise NoFilePathORNotExist,filepath
        self.__path = filepath
        
        
    
    
    def __read(self):
        if self.__load:
            return 
        with open(self.__path) as f:
            self.__content.extend([line.strip() for line in f.readlines()])
    
    
    def __parser(self):
        for line in self.__content:
            if not self.__empty(line):
                if line.startswith('#'):
                    pass
    
    def __empty(self ,  line):
        if not line or line.strip() == '':
            return True
        return False
            