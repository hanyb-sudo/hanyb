import os
import collections

def getAllDirBR(path):
    # 创建一个队列
    queue = collections.deque()
    # 先进行入队操作
    queue.append(path)

    # 当队列为空时结束循环
    while len(queue) != 0:
        # 将最初的路径进行出队
        dirpath = queue.popleft()
        # 得到目录下文件的列表
        filesList=os.listdir(dirpath)
        for fileName in filesList:
            absPath=os.path.join(dirpath,fileName)
            if os.path.isdir(absPath):
                print("目录："+fileName)
            #     进队列
                queue.append(absPath)
            else:
                print("普通："+fileName)



getAllDirBR(r"C:\Users\Lenovo\Desktop\数据挖掘实验")