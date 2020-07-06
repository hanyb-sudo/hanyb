import urllib.request
import re




#向指定的url地址发起请求，并返回服务器响应的数据(文件的对象)
response = urllib.request.urlopen("http://www.baidu.com")

#读取文件的全部内容，会把读取到的数据赋值给字符串变量
# data = response.read().decode("utf-8")
# print(type(data))

# re_title = re.compile("<title>.*?</title>")
# print(re_title.findall(data))

#读取一行
# data1 = response.readline()
# print(data1)

#读取文件的全部内容，把读取到的数据赋值给列表变量
# data2 = response.readlines()
# print(data2,"\n",len(data2))
# print(type(data2[100]))


# response 属性
#返回当前环境的相关信息
# print(response.info())


#返回状态码
print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
#     #处理网页信息
#     pass

#返回当前正在爬取的url
print(response.geturl())


url = "https://movie.douban.com/typerank?type_name=科幻&type=17&interval_id=100:90&action="

#编码
newUrl = urllib.request.quote(url)
print(newUrl)

#解码
newUrl2 = urllib.request.unquote(newUrl)
print(newUrl2)




