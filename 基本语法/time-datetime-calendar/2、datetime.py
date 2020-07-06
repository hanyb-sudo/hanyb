import datetime


# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))


# 获取指定时间
d2 = datetime.datetime(1997, 3, 26, 3, 23, 23)
print(d2)


# 将时间转为字符串
d3 = d1.strftime("%y-%m-%d %X")
print(d3)
print(type(d3))


# 将格式化字符串转为datetime对象
# 注意：转换的格式要与字符串一致
d4 = datetime.datetime.strptime(d3,"%y-%m-%d %X")
print(d4)
print(type(d4))


# 日期可以做减法
d5 = datetime.datetime(1997, 3, 26, 3, 23, 23)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)
print(type(d7))
# 间隔的天数,和间隔天数除外的秒数
print("间隔",d7.days,"days",d7.seconds,"seconds")