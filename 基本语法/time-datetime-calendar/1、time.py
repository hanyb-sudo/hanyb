import time

# 返回当前时间的时间戳，浮点数形式，不需要参数
c=time.time()
print(c)

# 将时间戳转为UTC时间元组
t=time.gmtime(c)
print(t)

# 将时间戳转为本地时间元组
b=time.localtime(c)
print(b)


# 将本地时间元组转为时间戳
m = time.mktime(b)
print(m)

# 将时间元组转为字符串
s = time.asctime(b)
print(s)


# 将时间戳转为字符串
p=time.ctime(c)
print(p)

# 将时间元组转成给定格式的字符串，参数2为时间元组，如果没有参数2，默认转当前时间
q = time.strftime("%Y-%m-%d %H:%M:%S",b)
print(q)
print(type(q))

# 将时间字符转转为时间元组
w = time.strptime(q, "%Y-%m-%d %H:%M:%S")
print(w)

# 延迟一个时间，整形或者浮点型
# time.sleep(4.1)


# 返回当前程序的cpu执行时间
# Unix始终返回全部的运行时间
# windows从第二次开始，都是以第一个调用此函数的时间戳作为基数
y1 = time.clock()
print("%d" % y1)
time.sleep(2)
y2 = time.clock()
print("%d" % y2)
time.sleep(2)
y3 = time.clock()
print("%d" % y3)

