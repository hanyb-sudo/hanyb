#爬糗事百科
import urllib.request
import ssl,re
import json,random

def wordCrawler(url):
    agentList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR"
    ]

    agentStr = random.choice(agentList)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", agentStr)

    # 使用ssl创建未验证的上下文,可以访问https的url
    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(req, context=context)

    jsonStr = response.read().decode("utf-8")
    # jsonData = json.loads(jsonStr)
    # print(type(jsonStr))
    return jsonStr


def dealData(str):
    re_word = re.compile(r'<div class="content">.<span>(.*?)</span>', re.S)
    wordList = re_word.findall(str)
    print(len(wordList))
    for words in wordList:
        print(words)


for i in range(1,11):
    url = r"https://www.qiushibaike.com/text/page/"+str(i)+"/"
    # url = r"https://www.qiushibaike.com/text/page/1/"
    data = wordCrawler(url)
    # print(data)
    dealData(data)
    # print("page %d finished！"%i)



