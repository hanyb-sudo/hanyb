import time

def run():
    while True:
        print("Hello Everyone!")
        time.sleep(2)


if __name__ == "__main__":
    while True:
        print("Hello Everybody!")
        time.sleep(2)


    #不会执行到run方法，只有上面的while循环执行结束才可以执行
    run()