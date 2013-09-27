#coding=utf-8

import os
from NewsCrawlerException import NewsCrawlerException

#文件操作类
#    
#
#
#
#

def _write(path,contents,mode):
    filehandle = open(path,mode)
    if not contents:
        raise NewsCrawlerException("DATA_IS_NONE",121)
    if isinstance(contents, list):
        for content in contents:
            filehandle.write(content)
    else:
        filehandle.write(contents)
    filehandle.close()
    
    
def append_write(path, contents):
    _write(path, contents, 'a')
    
def write_file(path,contents):
    _write(path, contents, 'w')
    
def clear_creat_write(path):
    _write(path,"")

def make_contents(contents):
    _contents = []
    if isinstance(contents, list):
        for content in contents:
            _contents.append("%s\n" % content.strip("\n"))
    return _contents

def make_dict_data(pattern,dictdata):
    if isinstance(dictdata, dict):
        restr = ''
        try:
            restr = pattern % dictdata
        except Exception,e:
            raise NewsCrawlerException("NO_RIGHT_PATTERN_%s" % e,109)
        return restr
    else:
        raise NewsCrawlerException("DATA_NO_DICT" ,110)
    

def _read(filepath):
    if not (os.path.isfile(filepath) and os.path.exists(filepath)):
        raise NewsCrawlerException("READ_FILE_WRONG_%s" % filepath , 111) 
    filehandle = open(filepath,"r")
    contents = filehandle.readlines()
    filehandle.close()
    return contents

def read_file_strip(filepath):
    _contents = _read(filepath)
    _newcontents = []
    for content in _contents:
        _newcontents.append(content.strip())
    return _newcontents

def read_file_line_format(filepath , formatfunction):
    _contents = _read(filepath)
    _newcontents = []
    for content in _contents:
        _newcontents.append(formatfunction(content))
    return _newcontents        



if __name__ == "__main__":
    contents = read_file_strip("/home/lixuze/result")
    diffcontents = []
    for content in contents:
        scontent = content.split("\t")
        if len(scontent) == 4:
            if  scontent[1] == scontent[2]:
                _content = "%s\t%s" % (scontent[1],scontent[0])
                diffcontents.append(_content)
    write_file("/home/lixuze/result_excute",make_contents(diffcontents))
    
        
        
    
