import urllib.request
import ssl
import re
import random
from collections import deque



def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)


def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w") as f:
        f.write(htmlBytes.decode("utf-8"))


def getResponse(url):
    agentList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR"
    ]

    agentStr = random.choice(agentList)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", agentStr)

    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()


def qqCrawler(url, toPath):
    htmlBytes = getResponse(url)
    htmlStr = str(htmlBytes)
    # writeFileBytes(htmlBytes, "qq.html")
    # pat = r'<div class="con">.*?<span>(.*?)</span>'
    pat_qq = r"[1-9]\d{5,9}"
    re_qq = re.compile(pat_qq, re.S)
    qqList = re_qq.findall(htmlStr)
    print("总共%d个qq号码"%len(qqList))
    for qq in qqList:
        with open(toPath, "a") as f:
            f.write(qq+"\n")
    pat_url = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    re_url = re.compile(pat_url)
    urlList = re_url.findall(htmlStr)
    # print(len(urlList))

    #去重
    urlList = list(set(urlList))

    return urlList


#中心控制器，队列进行广度遍历，遍历该url中的所有号码
def centerControl(url, toPath):
    queue = deque()
    queue.append(url)

    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            queue.append(item)





url = r"https://tieba.baidu.com/p/5924149874"
toPath = "qqFile.txt"
centerControl(url,toPath)

