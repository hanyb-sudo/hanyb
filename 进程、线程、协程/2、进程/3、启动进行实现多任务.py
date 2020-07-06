'''

multiprocessing 库

跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process
import time
import os


def run(str):
    while True:
        #os.getpid()获取当前进程id号
        #os.getppid()获取当前进程的父进程id号
        print("1、Hello Everyone!"+str,os.getpid(), "父进程号为：",os.getppid())
        time.sleep(2)


if __name__ == "__main__":
    print("主进程启动。。。",os.getpid())

    #创建一个子进程
    #target说明进程执行的任务
    p = Process(target=run, args=("你好！",))  #args要为可迭代对象
    #启动进程
    p.start()

    while True:
        print("2、Hello Everybody!",os.getpid())
        time.sleep(2)
