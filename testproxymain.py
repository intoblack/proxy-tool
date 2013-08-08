#coding=utf-8
#!/usr/bin/env python

import fileutil
from UrlQueue import TaskQueue
from assertproxy import AssertProxy
from ProxyData import ProxySave


contents = fileutil.read_file_strip("/home/lixuze/proxy.dat")

for line in contents:
    TaskQueue.getInstance().put(line)

p = ProxySave("/home/lixuze/valueproxy.dat")
p.start()

for i in range(30):
    a = AssertProxy()
    a.start()

    
    
    

