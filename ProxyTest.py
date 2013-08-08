#coding=utf-8


import urllib2




def open_url(url,host,port,keyword=None,timeout=2):
    isScuess = False
    try:
        proxy_handler = urllib2.ProxyHandler({"http" : 'http://%s:%s' % (host ,port)})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        content = urllib2.urlopen(url,timeout=timeout).read()
        if  keyword:
            if not content.find(keyword) == -1:
                isScuess = True
        else:
            isScuess = True
    except Exception,e:
        print e
    return isScuess

def read_host_port(filepath,splitword=':'):
    filehandle = open(filepath,'r')
    contents = filehandle.readlines()
    hostinfo = []
    for line in contents:
        if not line == "":
            line = line.strip()
            hostarry = line.split(splitword)
            if len(hostarry) == 2:
                hostinfo.append((hostarry[0],hostarry[1]))
    return hostinfo    

if __name__ == "__main__":
    print open_url('http://open.weibo.com/', "218.92.227.165","12945","新浪微博" , 1)
#     hostlist = []
#     for hostinfo in read_host_port('/home/lixuze/proxy.dat'):
#         isvalue = True
#         for i in range(3):
#             if not open_url('http://open.weibo.com/',hostinfo[0],hostinfo[1],"新浪微博",1):
#                 isvalue = False
#         if isvalue:
#             fileHandle = open("proxysave.dat","a")
#             fileHandle.write("%s:%s\n" % (hostinfo[0],hostinfo[1]))
#             fileHandle.close()
#             hostlist.append(hostinfo)
#     print hostlist
                
    
    
    
    