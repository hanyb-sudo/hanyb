import os
from multiprocessing import Pool
import time

def copyFile(path, toPath):
    with open(path, "rb") as fr:
        with open(toPath, "wb") as fw:
            text = fr.read()
            fw.write(text)


def copyByTradition(path, toPath):
    fileList = os.listdir(path)
    start = time.time()
    # 启动for循环进行处理每一个文件
    for fileName in fileList:
        copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))

    end = time.time()

    print("耗时:%.5f" % (end - start))





path = r"C:\Users\Lenovo\Desktop\python学习（公司）\进程、线程、协程\2、进程"

toPath =r"C:\Users\Lenovo\Desktop\python学习（公司）\进程、线程、协程\拷贝文件"
copyByTradition(path, toPath)


