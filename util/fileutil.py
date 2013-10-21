#coding=utf-8

import os
from ProxyException import NoFilePathException, NoDirPathException,\
    DataIsEmptyException,DataDictPatternException, NoKnowAboutException
import shutil
from Crypto.Util.py21compat import isinstance

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
#    if not os.path.isfile(path):
#        raise NoFilePathException,path
    with open(path,mode) as f:
        if isinstance(contents, list):
            [f.write(line) for line in contents]
        else:
            f.write(contents)
    
    
def append_write(path, contents):
    _write(path, contents, 'a')
    

def appen_write(path , contents):
    if isinstance(contents, list):
        __line = '\n'.join(contents)
    else:
        __line = contents 
    _write(path, __line, 'a')  
    
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
        except Exception:
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

def file_list(filedir,_level=0):
    filepath = []
    if os.path.isdir(filedir):
        item = (filedir, 'd',_level)
        filepath.append(item)
        for f in os.listdir(filedir):
            f = os.path.join(filedir, f)
            filepath.extend(file_list(f,_level+1))
    elif os.path.isfile(filedir):
        item = (filedir, 'f' ,_level)
        filepath.append(item)
    else:
        return []
    return filepath

def copy_path(src , dst , ingore = None):
    if  os.path.exists(src):
        if os.path.isfile(src) :
            if os.path.isfile(dst):
                shutil.copy(src, dst)
            else:
                raise NoFilePathException,dst
        elif os.path.isdir(src):
            if os.path.isdir(dst):
                shutil.copy(src,dst,ingore)
            else:
                raise NoDirPathException,dst
        else:
            raise NoKnowAboutException
    else:
        raise  NoFilePathException,src

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
    
        
        
    
