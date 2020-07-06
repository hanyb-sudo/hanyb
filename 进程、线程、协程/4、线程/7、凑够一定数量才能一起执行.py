import threading, time

bar = threading.Barrier(3)

def run():
    print("%s----start"%(threading.current_thread().name))
    time.sleep(1)

    #凑够一定数量才会执行wait下面的代码，没有凑够就一直等着
    bar.wait()
    print("%s----end" % (threading.current_thread().name))

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()