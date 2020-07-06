from multiprocessing import Process
import os, time

class HanybProcess(Process):
    def __init__(self, name):
        #调用父类中的构造函数的两种写法
        #写法1
        #super(HanybProcess, self).__init__()
        #写法2
        Process.__init__(self)
        self.name = name

    def run(self):
        print("子进程(%s--%s)启动"%(self.name, os.getpid()))

        #子进程的功能
        time.sleep(2)

        print("子进程(%s--%s)结束"%(self.name, os.getpid()))