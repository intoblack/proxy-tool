#-*- coding:utf-8 -*-
#!/usr/bin/env python


class IException(Exception):
    
    def __init__(self,msg='',code=None):
        self.msg = msg
        self.code = code
    
    def __str__(self):
        if self.code:
            return "%s,%s" % (self.msg,self.code)
        else:
            return "%s" % self.msg
    
    
class NoFilePathException(IException):
    pass


class NoDirPathException(IException):
    pass

class NoFileExistException(IException):
    pass

class DataIsEmptyException(IException):
    pass

class DataDictPatternException(IException):
    pass


if __name__ == "__main__":
    try:
        raise NoFileExistException,'x'
    except Exception,e:
        print e

