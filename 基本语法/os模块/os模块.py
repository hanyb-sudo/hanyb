import os

# 获取操作系统类型  nt->windows  posix->Linux或Mac OS X
print(os.name)

# 打印操作系统详细的信息，windows不支持
# print(os.uname())

# 获取操作系统中的所有环境变量
print(os.environ)


# 获取指定环境变量
print(os.environ.get("APPDATA"))

# 获取当前目录
print(os.curdir)

# 获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

#以列表的形式返回指定目录下的所有文件
print(os.listdir("../"))

# 在当前目录下创建新目录
# os.mkdir("han")

# 删除目录
# os.rmdir("han")

# 获取文件属性
print(os.stat("os概述.txt"))

# 重命名
# os.rename("han","hanyb")

# 删除普通文件
# os.remove("os概述.txt")

# 运行shell命令
# os.system("notepad")   #notepad，打开记事本
# os.system("write")
# os.system("shutdown -s -t 1")  #关机


# 有些模块存在os模块里，还有些存在于os.path里

# 查看当前的绝对路径
print(os.path.abspath("."))


# 拼接路径
p1=r"C:\Users\Lenovo\Desktop\python学习（公司）\os模块\os概述.txt"
p2=r"han"
# 注意：参数2里开始不要有斜杠
p3="D:/san/han"
p4="yi/bo"
print(os.path.join(p1,p2))
print(os.path.join(p3,p4))#D:/san/han\yi/bo  在linux系统中会变成D:/san/han/yi/bo


# 拆分路径
print(os.path.split(p1))

# 获取扩展名
print(os.path.splitext(p1))

# 判断是否是目录
print(os.path.isdir(p1))  #是则True，否则False

# 判断文件是否存在
print(os.path.isfile(p1))

# 判断目录是否存在
print(os.path.exists(p1))

# 获取文件大小(字节)
# print(os.path.getsize(p1),"字节")

# 文件的目录
print(os.path.dirname(p1))  #目录名
print(os.path.basename(p1))  #文件名

# 分离最后的目录或文件
# 注意：Windows下只能切文件，不能切目录
print(os.path.splitext(p1))



