import threading

'''
作用：为每个线程绑定一个数据库链接， HTTP请求，用户信息等，
这样一个线程的所有调用到的所有函数都可以非常方便地访问这些资源
'''
num = 0
#创建一个全局的ThreadLocal对象
#每个线程有独立的存储空间
#每个线程对ThreadLocal对象都可以读写，但是互不影响
local = threading.local()

def run(x, n):
    x = x + n
    x = x - n

def func(n):
    #每个线程都有local.x,就是线程的局部变量
    local.x = num
    for i in range(10000000):
        run(local.x, n)

    print(threading.current_thread().name,"----num = ",local.x)



if __name__ == "__main__":
    t1 = threading.Thread(target=func, args=(4, ))
    t2 = threading.Thread(target=func, args=(6, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num = ",num)