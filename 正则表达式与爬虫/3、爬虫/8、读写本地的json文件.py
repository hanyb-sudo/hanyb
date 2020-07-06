import json

def readJson():
    # 读取本地的json文件
    # 自动转成了字典形式
    path = r"movie.json"
    with open(path, "rb") as f:
        data = json.load(f)
        print(data)
        print(type(data))

#将python形式的数据写进本地json文件中
def writeJson():
    jsonData= {
    		"rate": "8.0",
    		"cover_x": 1400,
    		"title": "我是余欢水",
    		"url": "https:\/\/movie.douban.com\/subject\/33442331\/",
    		"playable": True,
    		"cover": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2574916002.jpg",
    		"id": "33442331",
    		"cover_y": 2139,
    		"is_new": False
    	}
    path = r"movies1.json"
    with open(path, "w") as f:
        json.dump(jsonData, f)




