#一个.py文件就是一个模块

'''
__name__属性：
模块就是一个可执行的.py文件，一个模块 被另一个程序引入。
我们不想让模块中某些代码执行，可以用__name__属性来使程序仅调用模块中的一部分
'''

# 每一个模块都有一个__name__属性，当其值等于“__main__”时，表明该模块自身在执行,否则被引入其他文件

# 当前文件如果为程序的入口文件，则__name__属性的值为__main__，当文件被引入其他文件时，__name__为文件名

if __name__ == "__main__":
    print(__name__)
    print("这是myModule.py文件！")
else:
    print(__name__)
    def sayHello():
        print("Hello boy!")

    def sayGoodBye():
        print("Bye Bye!")

