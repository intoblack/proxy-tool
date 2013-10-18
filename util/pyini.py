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

class PatternException(Exception):
    pass

class opinion():
    __opinion = ''
    __value = ''
    __coment = ''
    
    def __init__(self , key , value , comment = ''):
        self.__opinion = key
        self.__value = value
        self.__coment = comment 
        
    def __str__(self):
        return '%s=%s' % (self.__opinion , self.__value)

class comment():
    
    def __init__(self , comment):
        self.comment = comment
        
    def __str__(self):
        return self.comment
        

class Section():
    __opinions = {}
    __name = ''
    
    
    def get_sections(self):
        return self.__name
    
    def get_opinion(self , key):
        if self.__data.has_key(key):
            return self.__data['key']
        else:
            raise NoOpinionName,key
    
            

class Config():
    __data = {}
    
    def add_opinion(self,sectionname , key , value):
        if not self.__data.has_key(sectionname):
            self.__data[sectionname] = {}
        self.__data[sectionname][key] = value
    
    def __str__(self):
        _msg = ''
        for _sec,_opi in self.__data.items():
            _msg = '%s[%s]\n' % (_msg,_sec)
            for _key,_val in _opi.items():
                _msg = _msg + '%s=%s\n' % (_key,_val)
        return _msg
    

class PyIni(object):
    
    __path = None
    __content = []
    _config = Config()
    __load = False
    __comments = []
    __section_pattern = re.compile('\\[[\u4e00-\u9fa5a-zA-Z0-9_ ]+\\]', re.IGNORECASE)
    
    
    
    def __init__(self , filepath ,comment = '#' , config_split = '='):
        if not (filepath and os.path.exists(filepath) and os.path.isfile(filepath)):
            raise NoFilePathORNotExist,filepath
        self.__path = filepath
        self.__read()
        self.__parser()
        
        
    
    
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
                        _sectionname = section_match.group()[1:-1]
                    else:
                        raise SectionPatternException,line
                else:
                    opinionArry = line.split('=')
                    if opinionArry and len(opinionArry) == 2:
                        opinion(opinionArry[0], opinionArry[1])
                        self._config.add_opinion(_sectionname,opinionArry[0], opinionArry[1])
                    else:
                        raise PatternException,line
        return self._config
                        
                    
                        
                        
                    
                    
                    
                    
                
    
    def __empty(self ,  line):
        if not line or line.strip() == '':
            return True
        return False
if __name__ == "__main__":
    ini = PyIni('/home/lixuze/config.ini')
    print ini._config
    
            