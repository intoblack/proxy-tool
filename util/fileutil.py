#coding=utf-8

import os
from util.ProxyException import NoFilePathException, NoDirPathException,\
    DataIsEmptyException,DataDictPatternException

#文件操作类
#    
#
#
#
#



def is_file_exist(path):
    return os.path.isfile(path) and os.path.exists(path)

def is_dir_exist(path):
    return os.path.isdir(path) and os.path.exists(path)

def remove_file(path):
    if is_file_exist(path):
        os.remove(path)
    else:
        raise NoFilePathException,path

def remove_dir_down(path):
    if is_dir_exist(path):
        subpaths = os.listdir(path)
        for subpath in subpaths:
            os.remove(subpath)
    else:
        raise NoDirPathException,path


def _write(path,contents,mode):
    if not os.path.isfile(path):
        raise NoFilePathException,path
    with open(path,mode) as f:
        if isinstance(contents, list):
            [f.write(line) for line in contents]
        else:
            f.write(contents)
    
    
def append_write(path, contents):
    _write(path, contents, 'a')
    
def write_file(path,contents):
    if len(contents) ==0 or contents == None:
        raise DataIsEmptyException,contents
    _write(path, contents, 'w')
    
def clear_creat_write(path):
    if not os.path.isfile(path):
        raise NoFilePathException,path
    _write(path,"",'w')

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
            raise DataDictPatternException,pattern
        return restr
    else:
        raise DataDictPatternException,dictdata
    

def _read(filepath,mode='r'):
    if not is_file_exist(filepath):
        raise NoFilePathException,filepath
    contents = []
    with open(filepath,mode) as f:
        contents.extend(f.readlines())
    return contents



def read_file_strip(filepath):
    return [line.strip() for line in _read(filepath)]

def read_file_line_format(filepath , formatfunction):
    return [formatfunction(line) for line in _read(filepath)]    



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
    
        
        
    
