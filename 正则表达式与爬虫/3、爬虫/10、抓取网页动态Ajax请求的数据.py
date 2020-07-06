import urllib.request
import ssl
import json,random

def ajaxCrawler(url):
    agentList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR"
    ]

    agentStr = random.choice(agentList)
    req = urllib.request.Request(url)
    req.add_header("User-Agent",agentStr)

    #使用ssl创建未验证的上下文,可以访问https的url
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context= context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData
'''
url = r"https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"
info = ajaxCrawler(url)
print(info)
'''



for i in range(0,10):
    url = r"https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start="+str(i*20)+"&limit=20"
    info = ajaxCrawler(url)
    print(len(info))
    if len(info) == 0:
        break
