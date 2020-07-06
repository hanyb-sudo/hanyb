import urllib.request
import json,random
import ssl,os,re


def imageCrawler(url, toPath):
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
    htmlStr = response.read().decode("gbk")
    # print(type(htmlStr))
    # path = os.path.join(toPath, "image.html")
    # with open(path, "wb") as f:
    #     f.write(htmlStr)
    pat = r'<img.*((data-ks-lazyload)|(src))="(//.*?.jpg)"'
    re_image = re.compile(pat)
    imageList = re_image.findall(htmlStr)
    num =1
    for image in imageList:
        image_add = image[-1][:-10]
        image_path = os.path.join(toPath, str(num)+".jpg")
        num += 1
        # #把图片存到本地
        urllib.request.urlretrieve("http:"+image_add, image_path)



url = r"https://list.tmall.com/search_product.htm?spm=a221t.1476805.2109261262.4.27196769hFshwJ&q=%C1%AC%D2%C2%C8%B9&from=.list.pc_1_searchbutton&acm=lb-zebra-7419-257470.1003.4.405203&type=p&scm=1003.4.lb-zebra-7419-257470.OTHER_15182215355934_405203"
toPath = r"C:\Users\Lenovo\Desktop\python学习（公司）\正则表达式与爬虫\爬虫练习\女装image"

imageCrawler(url, toPath)


