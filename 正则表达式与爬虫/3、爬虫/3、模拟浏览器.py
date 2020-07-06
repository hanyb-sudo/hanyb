import urllib.request
import random


url = "http://www.baidu.com"
'''
#模拟请求头

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

}


# 设置一个请求体
req = urllib.request.Request(url, headers=headers)

#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)

'''

agentList =[
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR"
]

agentStr = random.choice(agentList)

# 添加请求头的第二种方式
req = urllib.request.Request(url)
#通过对应的键值向请求体中添加
req.add_header("User-Agent",agentStr)

response = urllib.request.urlopen(req)

data = response.read().decode("utf-8")
print(data)

'''
完整的请求头：
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Content-Type":"text/html;charset=utf-8",
    "X-Requested-With":"XMLHttpRequest"
}

'''

