from multiprocessing import Process
import time



def run():
    print("子进程开始")
    time.sleep(3)
    print("子进程结束")


if __name__ == "__main__":
    print("父进程启动。。。")
    p = Process(target=run)
    p.start()

    #父进程的结束不能影响子进程，让父进程等待子进程结束再执行父进程的结束
    p.join()
    print("父进程结束")
