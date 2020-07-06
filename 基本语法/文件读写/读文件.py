'''
path='读文件.txt'

f=open(path,"r",encoding="utf-8",errors="ignore")
print(f.read())
# print(f.read(10))

print("**********"*5)
f.seek(0)
print(f.read())
'''
# 一个完整的过程
'''
try:
    path='读文件.txt'

    f=open(path,"r",encoding="utf-8",errors="ignore")
    print(f.read())
finally:
    if f:  #判断是否存在f，存在才关闭，不存在就不做处理
        f.close()


# 简化：
path='读文件.txt'

with open(path,"r",encoding="utf-8",errors="ignore") as f1:
    print(f1.read())
'''
