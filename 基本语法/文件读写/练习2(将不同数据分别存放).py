import os

def writeFile(path, writeMethod, line):
    with open(path, writeMethod) as f:
        f.write(line)


path = r"C:\Users\Lenovo\Desktop\毕业论文\毕业论文数据\空气质量.txt"
keepPath = r"C:\Users\Lenovo\Desktop\python学习（公司）\文件读写\练习"

with open(path,"r") as f:
    # 将第一行的标题省略，让描述符跳到第二行
    f.readline()
    # 循环遍历读取的readlines里的内容
    for line in f.readlines():
        # 将地名作为我们的目录来保存信息
        dirName=line.split(" ")[0][1:-1]
        # 保存的绝对路径
        dirAbsPath = os.path.join(keepPath,dirName)
        # 文件的绝对路径
        docPath = os.path.join(dirAbsPath, dirName) + ".txt"
        if os.path.exists(dirAbsPath):
            writeFile(docPath,"a",line)
        else:
            # 如果目录不存在，则创建目录，并进行记录我们的信息
            os.mkdir(dirAbsPath)
            writeFile(docPath,"w",line)


