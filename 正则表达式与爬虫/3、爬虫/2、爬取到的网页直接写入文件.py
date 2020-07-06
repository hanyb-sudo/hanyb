import urllib.request

urllib.request.urlretrieve("http://www.baidu.com", filename=r"file.html")


#urlretrieve在执行的过程当中，会产生一些缓存
#清除缓存
urllib.request.urlcleanup()