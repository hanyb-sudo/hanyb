#Pool代表进程池，进行多个进程的管理
from multiprocessing import Pool
import time, os, random


def run(name):
    start = time.time()
    print("子进程%d启动--%s"%(name,os.getpid()))
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%d结束--%s--耗时%.3f"%(name,os.getpid(),end - start))

if __name__ == "__main__":
    print("父进程启动")

    #创建多个子进程
    #进程池
    #参数表示可以同时执行的进程数量
    #Pool默认大小是CPU核心数
    pp = Pool(4)    #默认本机CPU有4个核心数
    for i in range(3):
        #创建进程，放入进程池统一管理
        pp.apply_async(run, args=(i, ))

    #在使用进程池时，在调用join之前必须先调用close，调用close之后就不能再继续添加新的进程了
    pp.close()
    #进程池对象调用join，会等待进程池中的所有子进程结束完毕再去执行父进程
    pp.join()
    print("父进程结束")