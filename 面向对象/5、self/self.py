'''
self代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表哪个对象

self.__class__  代表类名

self不是关键字，换成其他标识符也是可以的，但是一般都用self
'''


class Person(object):
    def __init__(self, name, age, height, weight):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("run.....")

    def eat(self, food):
        print("eat " + food)

    def createObj(self):
        # 可以用self.__class__在类中创建本类对象
        print(self.__class__)
        p = self.__class__("Yan",22,165,53)
        print(p)

pre = Person("Hanne",22,180,60)
pre.createObj()
