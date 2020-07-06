'''

概念：一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的传输方式

json文件组成
{}  代表对象(字典)
[]  代表列表
:   代表键值对
,   分隔两个部分


'''
import json


jsonStr = '''{
		"rate": "8.0",
		"cover_x": 1400,
		"title": "我是余欢水",
		"url": "https:\/\/movie.douban.com\/subject\/33442331\/",
		"playable": true,
		"cover": "https://img3.doubanio.com\/view\/photo\/s_ratio_poster\/public\/p2574916002.jpg",
		"id": "33442331",
		"cover_y": 2139,
		"is_new": false
	}
'''

#将json格式的字符串转为python数据类型的对象
#将json格式数据转换为字典，方便取值
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(type(jsonStr))

jsonData2 = {
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

#将python数据类型的对象转换为json格式的字符串
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonData2))
print(type(jsonStr2))