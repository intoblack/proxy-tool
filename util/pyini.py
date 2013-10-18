#coding=utf-8
#!/usr/bin/env python

import os
import re

class NoFilePathORNotExist(Exception):
    pass

class NoOpinionName(Exception):
    pass

class SectionPatternException(Exception):
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
    __comments = []
    __section_pattern = re.compile('[\u4e00-\u9fa5a-zA-Z0-9_ ]', re.IGNORECASE)
    
    
    
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
        _sectionname = ''
        for line in self.__content:
            if not self.__empty(line):
                if line.startswith('#'):
                    self.__comments.append(line)
                elif line.startswith('[') and line.endswith(']'):
                    section_match = self.__section_pattern.match(line)
                    if section_match:
                        _sectionname = section_match[1:-1]
                    else:
                        raise SectionPatternException,line
                else:
                    opinionArry = line.split('=')
                    if opinionArry and len(opinionArry) == 2:
                        pass
                        
                    
                    
                    
                    
                
    
    def __empty(self ,  line):
        if not line or line.strip() == '':
            return True
        return False
if __name__ == "__main__":
    print '[az]'[1:-1]
            