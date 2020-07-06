'''

特点：把参数进行打包，单独传输

优点：数量大，安全(当对服务器数据进行修改时建议使用post)

缺点：速度慢

'''
import urllib.request
import urllib.parse
import random

url = r"http://202.115.140.232/"

#将要发送的数据合成一个字典
#字典的键去网址里找，一般为网页的name属性
data = {
    "UserId" : "*****",
    "Pwd" : "*******"
}
#对要发送的数据进行打包,要编码成bytes形式
postData = urllib.parse.urlencode(data).encode("gbk")

agentList =[
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR"
]

agentStr = random.choice(agentList)

#请求体
req = urllib.request.Request(url,data=postData)
req.add_header("User-Agent",agentStr)

#请求
response = urllib.request.urlopen(req)
data_qq = response.read()
print(data_qq)