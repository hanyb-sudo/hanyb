'''

析构函数：__del__()  释放对象时自动调用


'''

class Person(object):
    def __init__(self, name, age, height, weight):
        print("init runing......")
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("run.....")

    def eat(self, food):
        print("eat " + food)

    def __del__(self):
        print("del runing......")

per = Person("han", 22, 170, 60)
per.run()

# 释放对象
del per

# print(per.age)


# 在函数里定义的对象，会在函数结束时自动释放，这样可以用来减少内存空间的浪费
def func():
    per2 = Person("hh",1,1,2)

func()

while 1:
    pass
